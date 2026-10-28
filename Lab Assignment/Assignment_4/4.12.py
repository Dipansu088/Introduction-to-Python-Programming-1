# Accept numbers continuously and calculate their sum. Stop when the user enters 0

sum=0
while True:
    n=int(input("Enter number: "))
    if n==0:
        break
    sum=sum+n
    
print(sum)