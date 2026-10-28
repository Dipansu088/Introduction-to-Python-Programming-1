# Write a Python program to check whether a year is leap year or not.

n=int(input("Enter year: "))
if (n%400==0) or (n%4==0 and n%100!=0):
    print("leap yr")
else:
    print("not leap")