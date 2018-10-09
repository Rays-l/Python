#_*_ -coding:utf-8
import math
class regular:
    pi=3.14
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getzhouchang(self):
        self.zhouchang=self.__n*self.__side
    def getmianji(self):
        self.mianji=self.__n*pow(self.__side,2)/(4*math.tan(math.pi/self.__n))
    def show(self):
        print self.zhouchang
        print self.mianji
A=regular()
A.getzhouchang()
A.getmianji()
A.show()
B=regular(6,4)
B.getzhouchang()
B.getmianji()
B.show()
C=regular(10,4,5.6,7.8)
C.getzhouchang()
C.getmianji()
C.show()
