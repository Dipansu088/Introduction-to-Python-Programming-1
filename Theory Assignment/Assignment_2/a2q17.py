# Consider the list l1=[34, 10, 23, 44, 5, 7, 13, 39, 55, 12].Write a python program create two separate lists containing even numbers and odd numbers from l1.

l=[34, 10, 23, 44, 5, 7, 13, 39, 55, 12]

evenList=[]
oddList=[]

for i in l:
    if i%2==0:
       evenList.append(i)
    else:
        oddList.append(i) 
print(evenList)
print(oddList)