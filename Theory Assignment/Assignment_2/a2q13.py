# Write a program to check whether a number is divisible by both 5 and 11. Your output can be any one of the following:
# Number is divisible by both 5 and 11
# Number is divisible by 5 but not by 11
# Number is not divisible by 5 but divisible by 11
# Number is neither divisible by 5 nor 11.
# Write a python program to find the second largest among three numbers entered through keyboard.

n=int(input("Enter a number: "))
if n%5==0 and n%11==0:
    print("Number is divisible by both 5 and 11")
elif n%5==0 and n%11!=0:
    print("Number is divisible by 5 but not by 11")
elif n%5!=0 and n%11==0:
    print("Number is not divisible by 5 but divisible by 11")
else:
    print(f"Number is neither divisible by 5 nor 11.")
    
a=int(input("Enter a number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

if (a>=b and a<=c) or (a>=c and a<=b):
    second=a
elif (b>=a and b<=c) or (b>=c and b<=a):
    second=b
else:
    second=c
print(second)