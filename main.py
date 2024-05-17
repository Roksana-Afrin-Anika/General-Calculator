def calculator(num1,num2,c):
    if c == "+":
     add = num1 + num2
     print(f'Addition is : {add}')
    if c == "-":
     sub = num1 - num2
     print(f'Subtraction is : {sub}')
    if c == "*":
     mul = num1 * num2
     print(f'Multiplication is : {mul}')
    if c == "/":
     div = num1 / num2
     print(f'Division is : {div}')
    if c == "%":
     r = num1 % num2
     print(f'Remainder is : {r}')
    if c == "//":
     f = num1 // num2
     print(f'Floor is : {f}')


num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
c = input("Enter a choice from +,-,*,/,% and // : ")
calculator(num1,num2,c)
