'''Write a program to count how many times each digit occurs in a given number.'''

count=[0]*10
n=int(input("Enter a number: "))
while n>0:
    digit=n%10
    count[digit]+=1
    n=n//10

for i in range(10):
    if count[i]>0:
        print(f"{i} appears {count[i]} times.")