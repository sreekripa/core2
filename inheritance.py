# class student:
#     def __init__(self,name):
#         self.name=name
#     def getdata(self):
#         self.name=input("enter the name")
# class hod(student):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def putdata(self):
#         self.hodname=input("enter the hodname")
#     def display(self):
#         print("student name is",self.name)
#         print("hod name is",self.hodname)
# obj=hod('')
# obj.getdata()
# obj.putdata()
# obj.display()

# class A:
#     def __init__(self,name,hodname):
#         self.name=name
#         self.hodname=hodname
#     def getdata(self):
#         self.name=input("enter the name")
# class B(A):
#     def putdata(self):
#         self.hodname=input("enter the hod name")
#     def display(self):
#         print("student name is",self.name)
#         print("hod name is",self.hodname)
# class C(B):
#     def  fun3 (self):
#         print("hi avodha")
# class D(C):
#     def fun4 (self):
#         a=13
#         b=4
#         print(a+b)
# obj=D("","")
# obj.getdata()
# obj.putdata()
# obj.display()
# obj.fun3()
# obj.fun4()

class A:
    def get1(self):
        print("am A class")
class B:
    def get2(self):
        print("am B class")
class C(A,B):
    def get3(self):
        print("am inheritant A & B")
obj=C()
obj.get1()
obj.get2()
obj.get3()
