#_*_ -coding.utf-8
class Rectangle:
    def __init__ (self,wigth,height):
        self.wigth=wigth
        self.height=height
    def getArea(self):
        mianji = self.wigth*self.height
        print mianji
    def getPerimeter(self):
        zhouchang = 2*(self.wigth+self.height)
        print zhouchang

Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()



