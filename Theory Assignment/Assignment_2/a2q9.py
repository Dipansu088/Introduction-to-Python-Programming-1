# Write a program to check whether a number is an Automorphic number.

n=int(input("Enter: "))
square=n*n

if square%10==n:
    print("yes")
else:
    print("No")