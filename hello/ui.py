# -*- coding: utf-8 -*

from ScrolledText import ScrolledText
from Tkinter import *
import dangdang
import comments
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib

matplotlib.use('TkAgg')

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

thisbook = []


def getindex(index):
    if tszhonglei.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if price.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if zhekou.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if ccnt.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if cnum1.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if cnum2.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if cnum3.get() == '1':
        index.append(True)
    else:
        index.append(False)

    if cnumall.get() == '1':
        index.append(True)
    else:
        index.append(False)
    print(index)
    return index


def start():
    global thisbook
    print(v.get())
    if v.get() == '1':
        thisbook = dangdang.running(comments.ranksurl[0], 1)
    if v.get() == '2':
        thisbook = dangdang.running(comments.ranksurl[1], 1)
    if v.get() == '3':
        thisbook = dangdang.running(comments.ranksurl[2], 1)
    index = [True, True, True]
    thisindex = dangdang.getindex(getindex(index))
    for i in range(20):
        str = ''

        for j in thisindex:
            str += (thisbook[i].data[j] + ' ')

        str += '\n'
        text.insert('end', str)
    # text.insert('end','get');


def writeinexcel():
    index = [True, True, True]
    thisindex = dangdang.getindex(getindex(index))
    dangdang.writeinexcel(thisbook, thisindex)


root = Tk()
root.title('图书查询')

hours24 = IntVar()
May = IntVar()
years2017 = IntVar()

whichrank = Label(root, text='你要查询的排行：', font=('微软雅黑', 10))
whichrank.grid(row=0, column=0, pady=10)

v = StringVar()
v.set(0)

rankchoose1 = Radiobutton(root, text='24小时内', variable=v, value='1')
rankchoose1.grid(row=0, column=1, columnspan=5, sticky='w', padx=5)
rankchoose2 = Radiobutton(root, text='5月份', variable=v, value='2')
rankchoose2.grid(row=0, column=2, columnspan=5, sticky='w', padx=5)
rankchoose3 = Radiobutton(root, text='2017年', variable=v, value='3')
rankchoose3.grid(row=0, column=3, columnspan=5, sticky='w', padx=5)

whichrank = Label(root, text='你要查询的属性：', font=('微软雅黑', 10))
whichrank.grid(row=1, column=0, pady=10)

tszhonglei = StringVar()
price = StringVar()
zhekou = StringVar()
ccnt = StringVar()
cnum1 = StringVar()
cnum2 = StringVar()
cnum3 = StringVar()
cnumall = StringVar()

tszhonglei.set(0)
price.set(0)
zhekou.set(0)
ccnt.set(0)
cnum1.set(0)
cnum2.set(0)
cnum3.set(0)
cnumall.set(0)

kindchoose1 = Checkbutton(root, text=comments.allindex[3], variable=tszhonglei)
kindchoose1.grid(row=1, column=1, sticky='w', padx=5)

kindchoose2 = Checkbutton(root, text=comments.allindex[4], variable=price)
kindchoose2.grid(row=1, column=2, sticky='w', padx=5)

kindchoose3 = Checkbutton(root, text=comments.allindex[5], variable=zhekou)
kindchoose3.grid(row=1, column=3, sticky='w', padx=5)

kindchoose4 = Checkbutton(root, text=comments.allindex[6], variable=ccnt)
kindchoose4.grid(row=1, column=4, sticky='w', padx=5)

kindchoose5 = Checkbutton(root, text=comments.allindex[7], variable=cnum1)
kindchoose5.grid(row=1, column=5, sticky='w', padx=5)

kindchoose6 = Checkbutton(root, text=comments.allindex[8], variable=cnum2)
kindchoose6.grid(row=1, column=6, sticky='w', padx=5)

kindchoose7 = Checkbutton(root, text=comments.allindex[9], variable=cnum3)
kindchoose7.grid(row=1, column=7, sticky='w', padx=5)

kindchoose8 = Checkbutton(root, text=comments.allindex[10], variable=cnumall)
kindchoose8.grid(row=1, column=8, sticky='w', padx=5)

button = Button(root, text='开始', font=('微软雅黑', 10), command=start)
button.grid(row=0, column=5, padx=10)

button = Button(root, text='写入excel', font=('微软雅黑', 10), command=writeinexcel)
button.grid(row=0, column=6, padx=10)

figure1 = Figure(figsize=(5, 4), dpi=100)

canvas = FigureCanvasTkAgg(figure1, root)
canvas.get_tk_widget().grid(row=2, column=6, columnspan=5, padx=10, pady=10)


def draw():
    print('start')
    canvas = FigureCanvasTkAgg(figure1, root)
    canvas.get_tk_widget().grid(row=2, column=5, columnspan=5, padx=10, pady=10)
    plt = figure1.add_subplot(111)
    book = dangdang.getkind(thisbook, '图书种类')
    color = comments.cnames
    all = float(len(book))
    data = ()
    sizes = ()
    colors = ()
    explode = ()
    for key in book.keys():
        data = data + (key,)
        sizes = sizes + (book[key],)
        colors = colors + (color.popitem()[0],)
        explode = explode + (float(book[key]) / (all * 10),)
    plt.pie(sizes, explode=explode, labels=data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    canvas.show()


button = Button(root, text='分析', font=('微软雅黑', 10), command=draw)
button.grid(row=0, column=7, padx=10)

text = ScrolledText(root, font=('微软雅黑', 10))
text.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

root.mainloop()
