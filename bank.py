class bank():
    def __init__(self,acnt,name,typ,amt):
        self.ac=acnt
        self.nam=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name"=self.num)
        print("acnt num"=self.ac)
        print("acnt type"=self.type)
        print("bal=",self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("enter the name:")
t=input("enter the type")
a=int(input("enter number"))
am=int(input(input("enter the amount:"))
<<<<<<< HEAD
       obj=bank(a,n,t,am)
=======
obj=bank(a,n,t,am)
>>>>>>> ac8946f4d7899f1a6990f1cc780ecdcd318cc20a
print("account details")
obj.printamt()
w=int(input("enter amount to withdraw"))
print("b=",obj.with1(w))
