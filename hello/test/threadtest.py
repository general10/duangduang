# -*- coding:utf-8 -*-

import json
from bs4 import BeautifulSoup
import hello.dangdang as dd
import urllib2
import threading
import time
import hello.comments

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

    result[num] = comment

class MyThread(threading.Thread):

    def __init__(self, target, args):
        super(MyThread, self).__init__()  # 调用父类的构造函数
        self.target = target
        self.args = args

    def run(self):
        self.target(self.args)


def print_time(counter):
    while counter < 20:
        print "counter = %d" % counter
        getCommentCount(counter)
        print(result[counter])
        counter += 1
        # time.sleep(1)


def parse(thisbook):
    global bookurl
    bookurl = thisbook
    my_thread = MyThread(print_time, 0)
    my_thread.start()
    my_thread.join()


if __name__ == '__main__':
    parse(hello.comments.testbookurl)
