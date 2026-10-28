# Write a python program to print the prime factors of a given number.

n=int(input("Enter number: "))

for i in range(1,n):
    if n%i==0:
        print(i)