# Write a program that checks whether a given 3 digit number is an Armstrong number or not. A 3 digit number is an Armstrong number whose sum of the cubes of the digits is equal to the number itself. For Example, 370 =33 + 73 + 03
# Sample executions:
# Enter a number : 370
# Yes it is an Armstrong number
# Enter a number :450
# No it is not an Armstrong number

n=int(input("Enter a 3 digit number: "))
temp=n
sumofcubes=0

for i in range(n):
    digit=n%10
    sumofcubes=sumofcubes+(digit**3)
    n=n//10

if temp==sumofcubes:
    print("Armstrong")
else:
    print("Not a armstrong")