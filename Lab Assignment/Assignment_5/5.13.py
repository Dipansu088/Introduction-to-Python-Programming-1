# Write a program to input two lists and find the common elements between two lists without printing duplicates in the result.

l1=[]
l2=[]
n=int(input())
for i in range(n):
    num=int(input("Enter: "))
    l1.append(num)
    
for j in range(n):
    num=int(input("Enter: "))
    l2.append(num)
    
s1=set(l1)
s2=set(l2)
common=(s1|s2)
res=list(common)
print(res)