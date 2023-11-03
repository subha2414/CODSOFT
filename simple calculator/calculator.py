num1= float(input("Enter Number 1: "))
num2= float(input("Enter Number 2: "))
operator= input("Enter your choice: ")
if operator=='+':
    print("Addition of two number:")
    print(num1, "+", num2, "=",(num1+num2))
if operator=='-':
    print("Substraction of two number:")
    print(num1, "-", num2, "=",(num1-num2))
if operator=='*':
    print("Multiplication of two number:")
    print(num1, "*", num2, "=",(num1*num2))
if operator=='/':
    print("Division of two number:")
    print(num1, "/", num2, "=",(num1/num2))
if operator=='%':
    print("Modulus of two number:")
    print(num1, "%", num2, "=",(num1%num2))