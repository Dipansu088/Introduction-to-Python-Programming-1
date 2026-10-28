# Write a Python program to check whether a number is a palindrome.

n=int(input("Enter number: "))
rev=0
temp=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
    
if temp==rev:
    print("Pallindrome")
else:
    print("not a pallindrome")