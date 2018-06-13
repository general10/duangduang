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
        data = {}

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
    comment= {}
    comment['好评'] = summary['total_crazy_count']                    # 好评数
    comment['中评'] = summary['total_indifferent_count']              # 中评数
    comment['差评'] = summary['total_detest_count']                   # 差评数
    comment['好评率'] = summary['goodRate']                           # 好评率
    comment['图书种类'] = bk                                          # 图书种类
    return comment

def main():
    allindex = {'序号', '书名', '价格', '折扣', '评论数', '好评', '中评', '差评', '好评率'}
    choose =   {True, True, True, True, True, True, True, True, True}

    # wb = xlwt.Workbook()
    # sheet1 = wb.add_sheet("Sheet")
    # sheet1.write(0, 0, unicode('序号', "utf-8"))
    # sheet1.write(0, 1, unicode('书名', "utf-8"))
    # sheet1.write(0, 2, unicode('价格', "utf-8"))
    # sheet1.write(0, 3, unicode('折扣', "utf-8"))
    # sheet1.write(0, 4, unicode('评论数', "utf-8"))
    # sheet1.write(0, 5, unicode('好评', "utf-8"))
    # sheet1.write(0, 6, unicode('中评', "utf-8"))
    # sheet1.write(0, 7, unicode('差评', "utf-8"))
    # sheet1.write(0, 8, unicode('好评率', "utf-8"))

    book = ['']

    for page in range(2):

        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-%d' % (page+1)
        data = getdata(url)

        bookname = data.find_all('div', attrs={'class': 'name'})
        bookstar = data.find_all('div', attrs={'class': 'star'})
        bookprice = data.find_all('div', attrs={'class': 'price'})
        bookoff = data.find_all('span', attrs={'class': 'price_s'})


        for i in range(20):
            bookurl = bookname[i].find('a')['href']
            data = getCommentCount(bookurl)
            data['书名']
            print (str(page*20+i+1) + " "
                    + bookname[i].find('a')['title'] + " "                   # 书名
                    + data['图书种类'] + " "                                  # 图书种类
                    + bookprice[i].find('span').text[1:] + " "               # 价格
                    + bookoff[i].text[:-1] + " "                             # 折扣
                    + bookstar[i].find('a').text[:-3] + " "                  # 评论数
                    + data['好评'] + " "                                      # 好评数
                    + data['中评'] + " "                                      # 中评数
                    + data['差评'] + " "                                      # 差评数
                    + data['好评率'] + " "                                    # 好评率
                   )

            # sheet1.write(page * 20 + i + 1, 0, page * 20 + i + 1)
            # sheet1.write(page * 20 + i + 1, 1, bookname[i].find('a')['title'])
            # sheet1.write(page * 20 + i + 1, 2, bookprice[i].find('span').text[1:])
            # sheet1.write(page * 20 + i + 1, 3, bookoff[i].text[:-1])
            # sheet1.write(page * 20 + i + 1, 4, bookstar[i].find('a').text[:-3])
            # sheet1.write(page * 20 + i + 1, 5, data['好评'])
            # sheet1.write(page * 20 + i + 1, 6, data['中评'])
            # sheet1.write(page * 20 + i + 1, 7, data['差评'])
            # sheet1.write(page * 20 + i + 1, 8, data['好评率'])
            # wb.save('test.xls')


main()