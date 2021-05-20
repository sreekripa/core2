# x=lambda a:a+2
# print(x(3))
# def fun(a):
#     print(a+2)
# fun(5)
# x=lambda a,b:a*b
# print(x(2,4))
def multiply(n):
    return lambda a:a*n
num1=multiply(6)
print(num1(11))
num2=multiply(2)
print(num2(11))