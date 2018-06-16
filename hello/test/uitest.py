# -*- coding: utf-8 -*
from ScrolledText import ScrolledText
from Tkinter import *
import dangdang


root = Tk()
root.title('12306')

label_from_city = Label(root, text='出发城市', font=('微软雅黑', 10))
label_from_city.grid(row=0, column=0, ipady=10)
entry_from_city = Entry(root)
entry_from_city.grid(row=0, column=1, ipady=3)

label_to_city = Label(root, text='目的城市', font=('微软雅黑', 10))
label_to_city.grid(row=0, column=2, ipady=10)
entry_to_city = Entry(root)
entry_to_city.grid(row=0, column=3, ipady=3)

label_date = Label(root, text='出发日期', font=('微软雅黑', 10))
label_date.grid(row=0, column=4, ipady=10)
entry_date = Entry(root)
entry_date.grid(row=0, column=5, ipady=3)

sw = StringVar()
td = StringVar()
yd = StringVar()
rd = StringVar()
gr = StringVar()
rw = StringVar()
yw = StringVar()
rz = StringVar()
yz = StringVar()
sw.set(0)
td.set(0)
yd.set(0)
rd.set(0)
gr.set(0)
rw.set(0)
yw.set(0)
rz.set(0)
yz.set(0)

check_type_sw = Checkbutton(root, text='商务座', variable=sw)
check_type_sw.grid(row=1, column=0, columnspan=5, sticky='w',padx=10)

check_type_td = Checkbutton(root, text='特等座', variable=td)
check_type_td.grid(row=1, column=0, columnspan=5, sticky='w', padx=70)

check_type_yd = Checkbutton(root, text='一等座', variable=yd)
check_type_yd.grid(row=1, column=0, columnspan=5, sticky='w', padx=130)

check_type_rd = Checkbutton(root, text='二等座', variable=rd)
check_type_rd.grid(row=1, column=0, columnspan=5, sticky='w', padx=190)

check_type_gr = Checkbutton(root, text='高级软卧', variable=gr)
check_type_gr.grid(row=1, column=0, columnspan=5, sticky='w', padx=250)

check_type_rw = Checkbutton(root, text='软卧', variable=rw)
check_type_rw.grid(row=1, column=0, columnspan=5, sticky='e', padx=200)
check_type_yw = Checkbutton(root, text='硬卧', variable=yw)
check_type_yw.grid(row=1, column=0, columnspan=5, sticky='e', padx=150)
check_type_yz = Checkbutton(root, text='软座', variable=rz)
check_type_yz.grid(row=1, column=0, columnspan=5, sticky='e', padx=100)
check_type_yz = Checkbutton(root, text='硬座', variable=yz)
check_type_yz.grid(row=1, column=0, columnspan=5, sticky='e', padx=50)

button = Button(root, text='Start', font=('微软雅黑', 10), command=dosearch)
button.grid(row=1, column=5, columnspan=2, ipadx=10)

text = ScrolledText(root, font=('微软雅黑', 10))
text.grid(row=2, columnspan=6)


root.mainloop()