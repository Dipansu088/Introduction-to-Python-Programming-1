# Write a program to find the GCD of two numbers using loops without using math.gcd().

a=int(input("Enter: "))
b=int(input("Enter: "))

a=abs(a)
b=abs(b)

gcd=1
small=min(a,b)
for i in range(1, small+1):
    if a%i==0 and b%i==0:
        gcd=i
        
print(gcd)