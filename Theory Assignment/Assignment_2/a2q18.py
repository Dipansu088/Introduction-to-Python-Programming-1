# Search for a number in a list and display its index if found. Do not use the in operator for searching.

l=[]
n=int(input("Enter no of elements: "))
for i in range(n):
    num=int(input("Enter the no. "))
    l.append(num)
    
flag=False
search=int(input("Enter element to search: "))

for i in range(n):
    if l[i]==search:
        print(f"The number found at index: {i}")
        flag=True

if flag==False:
    print("Number not found!")