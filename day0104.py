class linear:
    def __init__ (self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def iss(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True
    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        print x
    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        print y

a,b,c,d,e,f=eval(raw_input('enter:a,b,c,d,e,f'))
A=linear(a,b,c,d,e,f)
if A.iss()!=True:
    print('The equation has on solution')
else:
    A.getX()
    A.getY()


