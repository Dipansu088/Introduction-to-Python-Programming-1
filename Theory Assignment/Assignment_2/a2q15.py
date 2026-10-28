# Write a python program to input a list of numbers and count the occurrences of each element without using collections.Counter.

n=int(input("Enter no of elements: "))
l=[]
l2={}
for i in range(n):
    num=int(input('Enter elements: '))
    l.append(num)
    
for num in l:
    if num in l2:
        l2[num]+=1
    else:
        l2[num]=1

for num in l2:
    print(f"{num} occurs {l2[num]} times.")