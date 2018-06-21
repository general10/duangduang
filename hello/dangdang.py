# -*- coding: utf-8 -*

import xlwt
from bs4 import BeautifulSoup
import re
import requests
import matplotlib
import time

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import comments
import mythread
import aboutmysql


class bookdata:
    def __init__(self):
        self.data = {}


def getJsonText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print '获取失败'
        return ''


def getdata(url):
    get = requests.get(url, headers=comments.header).text
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
    return comments.bookurltmp.format(productId=id['productId'],
                                      categoryPath=id['categoryPath'],
                                      mainProductId=id['mainProductId'])


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


def writeinexcel(book, index):
    wb = xlwt.Workbook()
    addtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    excelname = '%s.xls' % addtime
    sheet1 = wb.add_sheet("Sheet")

    for i in range(len(index)):
        sheet1.write(0, i, unicode(index[i], "utf-8"))

    for i in range(0, len(book)):
        for j in range(len(index)):
            sheet1.write(i + 1, j, book[i].data[index[j]])

    wb.save(excelname)
    aboutmysql.addtable(addtime)



def drawpic(book):
    color = comments.cnames
    all = float(len(book))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    data = ()
    sizes = ()
    colors = ()
    explode = ()
    for key in book.keys():
        data = data + (key,)
        sizes = sizes + (book[key],)
        colors = colors + (color.popitem()[0],)
        explode = explode + (float(book[key]) / (all * 10),)
    plt.figure(unicode('图书种类占比', "utf-8"))
    plt.pie(sizes, explode=explode, labels=data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()


def printbookinfo(bk):
    print (bk.data['序号'] + ' '
           + bk.data['书名'] + ' '  # 书名
           + bk.data['出版社'] + ' '  # 出版社
           + bk.data['图书种类'] + ' '  # 图书种类
           + bk.data['价格'] + ' '  # 价格
           + bk.data['折扣'] + ' '  # 折扣
           + bk.data['评论数'] + ' '  # 评论数
           + bk.data['好评'] + ' '  # 好评数
           + bk.data['中评'] + ' '  # 中评数
           + bk.data['差评'] + ' '  # 差评数
           + bk.data['好评率']  # 好评率
           )


def getkind(book, which):
    kind = {}

    for i in range(0, len(book)):
        kind[book[i].data[which]] = 0

    for i in range(0, len(book)):
        kind[book[i].data[which]] += 1

    sorted(kind.items(), key=lambda x: x[1], reverse=True)
    return kind


def running(rankurl, num):
    book = []
    for page in range(num):

        url = rankurl % (page + 1)
        data = getdata(url)

        bookname = data.find_all('div', attrs={'class': 'name'})
        bookstar = data.find_all('div', attrs={'class': 'star'})
        bookpublish = data.find_all('div', attrs={'class': 'publisher_info'})
        bookprice = data.find_all('div', attrs={'class': 'price'})
        bookoff = data.find_all('span', attrs={'class': 'price_s'})

        bookurl = {}
        bd = {}
        for i in range(20):
            bookurl[i] = bookname[i].find('a')['href']

        bd = mythread.parsebook(bookurl)

        for i in range(20):
            # bookurl = bookname[i].find('a')['href']
            index1 = page * 20 + i + 1
            # bd = getCommentCount(bookurl)
            bk = bookdata()
            bk.data['序号'] = str(index1)
            bk.data['书名'] = bookname[i].find('a')['title']
            bk.data['出版社'] = bookpublish[i * 2 + 1].find('a').text
            bk.data['图书种类'] = bd[i]['图书种类']
            bk.data['价格'] = bookprice[i].find('span').text[1:]
            bk.data['折扣'] = bookoff[i].text[:-1]
            bk.data['评论数'] = bookstar[i].find('a').text[:-3]
            bk.data['好评'] = str(bd[i]['好评'])
            bk.data['中评'] = str(bd[i]['中评'])
            bk.data['差评'] = str(bd[i]['差评'])
            bk.data['好评率'] = str(bd[i]['好评率'])
            book.append(bk)
    return book


def getindex(choose):
    index = []
    for i in range(0, len(comments.allindex)):
        if choose[i]:
            index.append(comments.allindex[i])
    return index


def draw(book):
    kind = getkind(book, '图书种类')
    drawpic(kind)


if __name__ == '__main__':
    choose = [True, True, True, True, True, True, True, True, True, True, True]
    # 选择要爬的东西
    index = getindex(choose)
    # 开始爬多少页 并存在book中
    book = running(comments.ranksurl[1], 1)
    # 写入excel
    writeinexcel(book, index)
    # 画图
    draw(book)
