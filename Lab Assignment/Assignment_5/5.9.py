# Write a Python program to input a list of n numbers and calculate their sum and average without using sum().

def calculate(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        avg=sum/len(numbers)
    return sum, avg

n=int(input("Enter no. of elements: "))
numbers=[]
for i in range(n):
    num=int(input("Enter numbers: "))
    numbers.append(num)
    
result=calculate(numbers)
print(f"Sum: {result[0]}")
print(f"Average: {result[1]}")