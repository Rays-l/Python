#_*_ -coding.utf-8
class Account:
    def __init__(self,id,balance,annual):
        self.__id=id
        self.__balance=balance
        self.__annual=annual/100
    def getlilv(self):
        self.lilv=self.__annual/12
    def getlixi(self):
        self.lixi=self.__balance*self.__annual/12
    def withdraw(self,new):
        self.__balance=self.__balance-new
    def show(self):
        print self.__id
        print self.__balance
        print self.lilv
        print self.lixi
AC=Account(1122,20000,4.5)
AC.getlilv()
AC.getlixi()
AC.withdraw(2500)
AC.withdraw(-3000)
AC.show()

