class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdata(self):
        self.name=input("enter the name")
        self.mark=input("enter the mark")
    def putdata(self):
        print(self.name,"\n",self.mark)
obj=student('','')
obj.getdata()
obj.putdata()



