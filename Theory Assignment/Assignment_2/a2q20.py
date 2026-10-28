# Consider the lists: . l1 = [12, 14, 10, 4, 67, 34, 14 and l2=[55, 11, 34, 12, 15, 11]Write a python program to find the unique elements present in both the lists. (Hine: convert the list to a set)

l1 = [12, 14, 10, 4, 67, 34, 14]
l2 = [55, 11, 34, 12, 15, 11]

s1=set(l1)
s2=set(l2)
common=(s1 & s2)
print(common)