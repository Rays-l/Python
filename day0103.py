#_*_ -coding:utf-8
class fan:
    def __init__ (self,speed=1,kai="false",radius=5,color="bule"):
        self.__speed=speed
        self.__kai=kai
        self.__radius=radius
        self.__color=color
    def show(self):
        print self.__speed
        print self.__kai
        print self.__radius
        print self.__color
fan(3,"on",10,"yellow").show()
fan(2,"false").show()
