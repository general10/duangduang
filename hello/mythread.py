# -*- coding:utf-8 -*-

import json
from bs4 import BeautifulSoup
import dangdang as dd
import urllib2
import threading
import time
import comments

result = {}

bookurl = {}

def getCommentCount(num):
    url = bookurl[num]

    html = urllib2.urlopen(url).read()

    # 用正则表达式获取对应id
    id = dd.getId(html)

    # 拼接ajax对应的url
    json_url = dd.getCommentUrl(id)

    # 获取url对应的json
    json_html = json.loads(dd.getJsonText(json_url))

    # 获取图书种类
    data = BeautifulSoup(html, 'lxml')
    bookkind = data.find_all('span', attrs={'class': 'lie'})[0].text
    bk = dd.getbookkind(bookkind)

    # 获取评论数
    summary = json_html['data']['list']['summary']
    comment = {}
    comment['好评'] = summary['total_crazy_count']                    # 好评数
    comment['中评'] = summary['total_indifferent_count']              # 中评数
    comment['差评'] = summary['total_detest_count']                   # 差评数
    comment['好评率'] = summary['goodRate']                           # 好评率
    comment['图书种类'] = bk                                          # 图书种类
    global result
    result[num] = comment


# -*- coding:utf-8 -*-

import threading, thread
import time


class MyThread(threading.Thread):

    def __init__(self, target, args):
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.target = target
        self.args = args

    def run(self):
        self.target(self.args)


def getcomment(counter):
    while counter < 20:
        print "counter = %d" % counter
        getCommentCount(counter)
        print(result[counter])
        counter += 2
        # time.sleep(1)


def parsebook(thisbook):
    global bookurl
    bookurl = thisbook

    my_thread1 = MyThread(getcomment, 0)
    my_thread2 = MyThread(getcomment, 1)

    my_thread1.start()
    my_thread2.start()

    my_thread1.join()
    my_thread2.join()
    return result

if __name__ == '__main__':
    parsebook(comments.testbookurl)
