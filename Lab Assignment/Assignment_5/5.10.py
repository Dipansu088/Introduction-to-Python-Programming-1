# Write a Python program to input a list of n numbers and find the largest and smallest numbers in a list without using max() or min().

n=int(input("No. of elements: "))
numbers=[]

for i in range(n):
    num=int(input())
    numbers.append(num)
    
largest=numbers[0]
smallest=numbers[1]
    
for i in numbers:
    if i>largest:
        largest=i
        
    if i<smallest:
        smallest=i
        
print(largest, smallest)