# -*- coding: utf-8 -*
from ScrolledText import ScrolledText
from Tkinter import *
# import dangdang

import sys
import tkinter as Tk
import matplotlib
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
root =Tk.Tk()
root.title("matplotlib in TK")
#设置图形尺寸与质量
f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0,3,0.01)
s = sin(2*pi*t)
#绘制图形
a.plot(t, s)
#把绘制的图形显示到tkinter窗口上
canvas =FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
toolbar =NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#定义并绑定键盘事件处理函数
def on_key_event(event):
    print('you pressed %s'% event.key)
    key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect('key_press_event', on_key_event)
#按钮单击事件处理函数
def _quit():
#结束事件主循环，并销毁应用程序窗口
    root.quit()
    root.destroy()
    button =Tk.Button(master=root, text='Quit', command=_quit)
    button.pack(side=Tk.BOTTOM)
Tk.mainloop()

# from tkinter import Tk, Canvas
#
#
# def DrawPie():
#     # 创建窗口
#     windows = Tk()
#
#     # 添加标题
#     windows.title("画饼图")
#
#     # 设置画布样式
#     canvas = Canvas(windows, height=500, width=500)
#
#     # 将画布打包到窗口
#     canvas.pack()
#
#     # 利用画布的create_arc画饼形，(400,400)和(100,100)为饼形外围的矩形,
#     # start=角度起始，extent=旋转的度数，fill=填充的颜色
#     canvas.create_arc(400, 400, 100, 100, start=0, extent=36, fill="red")
#     canvas.create_arc(400, 400, 100, 100, start=36, extent=72, fill="green")
#     canvas.create_arc(400, 400, 100, 100, start=108, extent=108, fill="yellow")
#     canvas.create_arc(400, 400, 100, 100, start=216, extent=144, fill="blue")
#
#     # 为各个扇形添加内容，圆心为（250，250）
#     canvas.create_text(430, 200, text="36°", font=("华文新魏", 20))
#     canvas.create_text(330, 100, text="72°", font=("华文新魏", 20))
#     canvas.create_text(90, 200, text="108°", font=("华文新魏", 20))
#     canvas.create_text(390, 370, text="144°", font=("华文新魏", 20))
#
#     # 开启消息循环
#     windows.mainloop()
#
#
# if __name__ == '__main__':
#     # 调用方法
#     DrawPie()

# root = Tk()
# root.title('12306')
#
# label_from_city = Label(root, text='出发城市', font=('微软雅黑', 10))
# label_from_city.grid(row=0, column=0, ipady=10)
# entry_from_city = Entry(root)
# entry_from_city.grid(row=0, column=1, ipady=3)
#
# label_to_city = Label(root, text='目的城市', font=('微软雅黑', 10))
# label_to_city.grid(row=0, column=2, ipady=10)
# entry_to_city = Entry(root)
# entry_to_city.grid(row=0, column=3, ipady=3)
#
# label_date = Label(root, text='出发日期', font=('微软雅黑', 10))
# label_date.grid(row=0, column=4, ipady=10)
# entry_date = Entry(root)
# entry_date.grid(row=0, column=5, ipady=3)
#
# sw = StringVar()
# td = StringVar()
# yd = StringVar()
# rd = StringVar()
# gr = StringVar()
# rw = StringVar()
# yw = StringVar()
# rz = StringVar()
# yz = StringVar()
# sw.set(0)
# td.set(0)
# yd.set(0)
# rd.set(0)
# gr.set(0)
# rw.set(0)
# yw.set(0)
# rz.set(0)
# yz.set(0)
#
# check_type_sw = Checkbutton(root, text='商务座', variable=sw)
# check_type_sw.grid(row=1, column=0, columnspan=5, sticky='w',padx=10)
#
# check_type_td = Checkbutton(root, text='特等座', variable=td)
# check_type_td.grid(row=1, column=0, columnspan=5, sticky='w', padx=70)
#
# check_type_yd = Checkbutton(root, text='一等座', variable=yd)
# check_type_yd.grid(row=1, column=0, columnspan=5, sticky='w', padx=130)
#
# check_type_rd = Checkbutton(root, text='二等座', variable=rd)
# check_type_rd.grid(row=1, column=0, columnspan=5, sticky='w', padx=190)
#
# check_type_gr = Checkbutton(root, text='高级软卧', variable=gr)
# check_type_gr.grid(row=1, column=0, columnspan=5, sticky='w', padx=250)
#
# check_type_rw = Checkbutton(root, text='软卧', variable=rw)
# check_type_rw.grid(row=1, column=0, columnspan=5, sticky='e', padx=200)
# check_type_yw = Checkbutton(root, text='硬卧', variable=yw)
# check_type_yw.grid(row=1, column=0, columnspan=5, sticky='e', padx=150)
# check_type_yz = Checkbutton(root, text='软座', variable=rz)
# check_type_yz.grid(row=1, column=0, columnspan=5, sticky='e', padx=100)
# check_type_yz = Checkbutton(root, text='硬座', variable=yz)
# check_type_yz.grid(row=1, column=0, columnspan=5, sticky='e', padx=50)
#
# button = Button(root, text='Start', font=('微软雅黑', 10), command=dosearch)
# button.grid(row=1, column=5, columnspan=2, ipadx=10)
#
# text = ScrolledText(root, font=('微软雅黑', 10))
# text.grid(row=2, columnspan=6)
#
#
# root.mainloop()