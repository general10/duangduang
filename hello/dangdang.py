# -*- coding: utf-8 -*

import urllib2
import xlwt
from bs4 import BeautifulSoup
from datashape import json
import re
import json
import requests

class bookdata:
    def __init__(self):
        self.data = {}

def getJsonText(url):
    try:
        r = requests.get(url, timeout=1)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print '获取失败'
        return ''

def getdata(url):
    get = urllib2.urlopen(url).read()
    data = BeautifulSoup(get, 'lxml')
    return data


def getId(html):
    id = {}
    ma = re.search(r'"productId":"[\d]+"', html)
    id['productId'] = eval(ma.group().split(':')[-1])
    ma = re.search(r'"categoryPath":"[\d.]+"', html)
    id['categoryPath'] = eval(ma.group().split(':')[-1])
    ma = re.search(r'"mainProductId":"[\d.]+"', html)
    id['mainProductId'] = eval(ma.group().split(':')[-1])
    return id

def getCommentUrl(id):
    return 'http://product.dangdang.com/index.php?r=comment%2Flist&productId={productId}&categoryPath={categoryPath}&mainProductId={mainProductId}&mediumId=0&pageIndex=1&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0'.format(
        productId=id['productId'], categoryPath=id['categoryPath'], mainProductId=id['mainProductId'])

def getbookkind(str):
    res = ''
    cnt = 0
    for i in str:
        if i == '>':
            cnt += 1
        if cnt > 1:
            break
        if (cnt == 1) and (i != '>'):
            res += i
    return res

def writeinexcel(book,index):
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet("Sheet")

    for i in range(len(index)):
        sheet1.write(0, i, unicode(index[i], "utf-8"))

    for i in range(0, len(book)):
        for j in range(len(index)):
            sheet1.write(i+1, j, book[i].data[index[j]])

    wb.save('test.xls')

def getCommentCount(url):
    html = urllib2.urlopen(url).read()

    # 用正则表达式获取对应id
    id = getId(html)

    # 拼接ajax对应的url
    json_url = getCommentUrl(id)

    # 获取url对应的json
    json_html = json.loads(getJsonText(json_url))

    # 获取图书种类
    data = BeautifulSoup(html, 'lxml')
    bookkind = data.find_all('span', attrs={'class': 'lie'})[0].text
    bk = getbookkind(bookkind)

    # 获取评论数
    summary = json_html['data']['list']['summary']
    comment = {}
    comment['好评'] = summary['total_crazy_count']                    # 好评数
    comment['中评'] = summary['total_indifferent_count']              # 中评数
    comment['差评'] = summary['total_detest_count']                   # 差评数
    comment['好评率'] = summary['goodRate']                           # 好评率
    comment['图书种类'] = bk                                          # 图书种类
    return comment

def printbookinfo(bk):
    print (bk.data['序号'] + ' '
            + bk.data['书名'] + ' '                                     # 书名
            + bk.data['出版社'] + ' '                                   # 出版社
            + bk.data['图书种类'] + ' '                                 # 图书种类
            + bk.data['价格'] + ' '                                     # 价格
            + bk.data['折扣'] + ' '                                     # 折扣
            + bk.data['评论数'] + ' '                                   # 评论数
            + bk.data['好评'] + ' '                                     # 好评数
            + bk.data['中评'] + ' '                                     # 中评数
            + bk.data['差评'] + ' '                                     # 差评数
            + bk.data['好评率']                                         # 好评率
           )

if __name__ == '__main__':
    allindex = ['序号', '书名', '出版社', '图书种类', '价格', '折扣', '评论数', '好评', '中评', '差评', '好评率']
    allchoose = [True, True, True, True, True, True, True, True, True, True, True]

    index = []
    for i in range(0,len(allindex)):
        if allchoose[i]:
            index.append(allindex[i])

    book = []
    for page in range(1):

        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-%d' % (page+1)
        data = getdata(url)

        bookname = data.find_all('div', attrs={'class': 'name'})
        bookstar = data.find_all('div', attrs={'class': 'star'})
        bookpublish = data.find_all('div', attrs={'class': 'publisher_info'})
        bookprice = data.find_all('div', attrs={'class': 'price'})
        bookoff = data.find_all('span', attrs={'class': 'price_s'})


        for i in range(5):
            bookurl = bookname[i].find('a')['href']
            index1 = page*20+i+1
            bd = getCommentCount(bookurl)
            bk = bookdata()
            bk.data['序号'] = str(index1)
            bk.data['书名'] = bookname[i].find('a')['title']
            bk.data['出版社'] = bookpublish[i * 2 + 1].find('a').text
            bk.data['图书种类'] = bd['图书种类']
            bk.data['价格'] = bookprice[i].find('span').text[1:]
            bk.data['折扣'] = bookoff[i].text[:-1]
            bk.data['评论数'] = bookstar[i].find('a').text[:-3]
            bk.data['好评'] = str(bd['好评'])
            bk.data['中评'] = str(bd['中评'])
            bk.data['差评'] = str(bd['差评'])
            bk.data['好评率'] = str(bd['好评率'])
            book.append(bk)

    writeinexcel(book, index)
