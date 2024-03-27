class hello():
    def function(self,b):
        self.choice=int(input("Enter the choice: "))
        self.choice1=int(input("Enter the choice: "))
        self.cb=100+b
    def glass(self,h,f,d):
        hf=self.cb+h+f+d
        c=self.choice+self.choice1
        print(c,hf)
x=hello()
h=100
x.function(h)
x.glass(100,200,200)