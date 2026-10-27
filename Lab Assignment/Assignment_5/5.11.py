# Write a Python program to input a list of n numbers and reverse the list using a loop, but
# without using slicing or the built-in reverse() method.

n=int(input("No. of elements: "))
numbers=[]
rev=[]

for i in range(n):
    num=int(input())
    numbers.append(num)
    
for i in numbers:
    rev=[i]+rev
print(rev)