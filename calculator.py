def calculator():
    print("welcom to basuc calculator")
    num1 =float(input("enter first number"))
    num2 =float(input("enter second number"))
    operator=input("enter the operation(+,*,-<,/)")

    if operator == '+':
        print(f"The result is :{num1+num2}")

    elif operator == '-':
        print(f"The result is :{num1-num2}")
    
    elif operator =='*':
        print(f"The result is :{num1*num2}")

    elif operator == '/':
        print(f"The result is {num1/num2}")

    else :
        print("invalid input")

calculator()