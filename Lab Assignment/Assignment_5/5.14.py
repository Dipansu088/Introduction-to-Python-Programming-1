# Write a Python program to input a list of n numbers and count the occurrences of each element without using any predefined class.

l=[]
n=int(input("Enter number: "))
for i in range(n):
    num=int(input("Enter"))
    l.append(num)
    
for j in set(l):
    count=0
    for k in l:
        if j==k:
            count=count+1
    if count>0:
        print(j,":",count)