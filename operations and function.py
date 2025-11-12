num1 = float(input("Enter your first number:  "))
num2 = float(input("Enter your second number:  "))
op = input("Enter op:  ")
def Sum(num1,num2):
    sum=num1+num2
    print(sum)
Sum(num1,num2)

def Div(num1,num2):
    div=num1/num2
    print(div)
Div(num1,num2)

def Mult(num1,num2):
    res=num1*num2
    print(res)
Mult(num1,num2)

def Sub(num1,num2):
    res=num1-num2
    print(res)
Sub(num1,num2)

def Calc(num1,num2,op):
    if op== "/":
        Div(num1,num2)
    elif op== "*":
        Mult(num1,num2)
    elif op== "+":
        Sum(num1,num2)
    elif op== "-":
        Sub(num1,num2)
    else:
        print("enter valid op")

Calc(num1,num2,op)
