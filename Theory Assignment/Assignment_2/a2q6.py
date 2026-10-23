'''Write a python program to print all prime numbers between 1-500.'''

for num in range(2,501):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)