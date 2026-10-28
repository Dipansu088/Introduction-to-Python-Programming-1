# Check whether a number is positive and then determine whether it is even or odd.

n=int(input("Enter number: "))
if n>0:
    print("+ve")
else:
    print("-ve")
    
if n%2==0:
    print("Even")
else:
    print("Odd")