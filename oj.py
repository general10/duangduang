import sys

class data:

    def __init__(self,num):
        self.a = {}
        self.a[1] = num

if __name__ == '__main__':
    dt1 = []

    dt1.append(data(2))
    dt1.append(data(3))
    dt1.append(data(4))

    for i in range(3):
        print(dt1[i].a[1])

    dt1[1].a[1]=100

    for i in range(3):
        print(dt1[i].a[1])