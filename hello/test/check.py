# coding: utf-8

import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import hello.comments

def write(book):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    color = hello.comments.cnames
    data = ()
    sizes = ()
    colors = ()
    for key in book.keys():
        data = data + (unicode(key, "utf-8"),)
        sizes = sizes + (book[key],)
        colors = colors + (color.popitem()[0],)
    print(data)
    print(sizes)
    print(colors)
    plt.figure(unicode('图书种类占比', "utf-8"))
    plt.pie(sizes,  labels=data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()


def example():
    labels = ('second', 'third', 'first')
    sizes = (1, 5, 2)
    colors = ('indigo', 'gold', 'hotpink')
    explode = 0, 0, 0, 0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    # example()
    book = {}
    book['小说'] = 2
    book['童话'] = 1
    book['传记'] = 5
    sorted(book.items(),key = lambda x:x[1],reverse = True)
    write(book)

