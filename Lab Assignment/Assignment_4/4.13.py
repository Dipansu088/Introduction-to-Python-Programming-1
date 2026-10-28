# For a given x and a given n, write a python program to compute xn/n!.

x=int(input("Enter x: "))
n=int(input("Enter n: "))

fact=1
for i in range(1,n+1):
    fact=fact*i
    
result=(x**n)/fact
print(result)