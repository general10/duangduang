## 爬虫爬当当网书籍信息

---

### 关于包的几点说明

- 本爬虫基于py2.7(电脑里anaconda3一直没安装成功就没用py3.6

- mysqldb不能从pycharm直接安装 要去官网下

    具体安装包在自己电脑里 等下次有网了传上来

- 代码里用urllib2和request并没有本质区别

- 推荐安装anaconda2 省时省力= =

---

### 具体介绍

#### 作业要求是五部分

#####  图形界面

#####  多线程

#####  文件操作

#####  数据库操作

#####  网络编程

#### 额外要求

#####  数据可视化

---

### 运行效果

![image](https://github.com/general10/duangduang/blob/master/hello/test/pic.jpg)

---

commments里是一些蛋疼的常量

有的.py里可能有调试的main= =

可以试着玩一玩

---
### 图形界面

ui.py

用 Tkinter 实现 感觉挺丑的 但是是在没啥可以优化的点了

（这东西就这么丑没办法= =）

重点是和画图的 matplotlib 结合起来冲突

好像是共用了某一线程（？）

解决了一下午

最后创建一个 canvas 画板 在这个画板里面画

还有就是多个按钮的坑 不知道怎么for出来 就一个一个写了

---

### 多线程 

mythread.py

一个爬奇数 一个爬偶数

把函数和参数都传进去就让他自己high就行了= =

（傻瓜式多线程）

---

### 文件操作

写入excel也算是文件操作= =

百度下哪个参数什么意思就行了

---

### 数据库操作

aboutmysql.py

数据库操作加的比较急 是回去下了火车才加的

因为编码原因 为了用而用的（.xls都加不进去我有什么办法= =）

所以插入的是 插入时间 和 更新时间 一般来说这两个时间都是一样的（还没见过不一样的时候）

后续可以加上某次爬的内容

---

### 网络编程

dangdang.py

爬虫本身没啥好讲的（感觉这不叫网络编程啊= =）

详见：https://www.cnblogs.com/general10/p/8979389.html

---

### 数据可视化

matplotlib 最大的问题是和 Thinter 结合

随便拼一拼就能用了 本身并不难
