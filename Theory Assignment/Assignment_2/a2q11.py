# Create a simple calculator using if-elif-else

a=float(input("Enter 1st no. "))
b=float(input("Enter 2nd no. "))
op=input("Enter operation: ")

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="%":
    print(a%b)
else:
    print("Enter within +, -, /, *, %")