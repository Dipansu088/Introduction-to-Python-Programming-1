'''Write a Python program to input 10 numbers and find the largest number using for loop.'''

largest=None
for i in range(10):
    n=int(input("Enter number: "))
    
    if largest==None or n>largest:
        largest=n
print(largest)