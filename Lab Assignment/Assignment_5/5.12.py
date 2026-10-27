# Write a function in python that takes a list of values as input parameter and returns another list without any duplicates. (do not convert the list into a set.)

n=int(input())
numbers=[]
new=[]

for i in range(n):
    num=int(input("Enter numbers: "))
    numbers.append(num)
    
for i in numbers:
    if i not in new:
        new.append(i)
print(new)