# Write a python program to generate and print the first n terms of the Fibonacci sequence where n>=1. The first few terms are: 0, 1, 1, 2, 3, 5, 8, 13, …….…..

n=int(input("Enter number: "))
a=0
b=1
for i in range(n):
    print(a)
    s=a+b
    a=b
    b=s
    