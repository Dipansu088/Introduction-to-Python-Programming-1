# Write a python program to initialize two lists and find the common elements between two lists without printing duplicates in the result.

l1=[1,2,3,1,6,22]
l2=[4,1,9,4,2,7]

s1=set(l1)
s2=set(l2)

common=(s1|s2)
print("Common: ",list(common))