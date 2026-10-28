# Write a program to count the number of digits in a given number.

n=int(input("Enter a number: "))

count=len(str(abs(n)))
print(count)