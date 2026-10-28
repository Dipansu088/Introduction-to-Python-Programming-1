# Write a python program to input a number and check whether it is a prime number or not?

n=int(input("Enter number: "))

if n>=2:
    isPrime=True
    for i in range(2,n):
        if n%i==0:
            isPrime=False
            break
    if isPrime:
        print("Prime")
    else:
        print("Not a prime")
else:
    print("Enter no. above 1")