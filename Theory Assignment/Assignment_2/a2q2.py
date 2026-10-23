'''Input 10 numbers and count how many are even and how many are odd.'''

even=0
odd=0
for i in range(10):
    n=int(input("Enter a number: "))
    if n%2==0:
        even+=1
    else:
        odd+=1
print(f"Even count is: {even}")
print(f"Odd count is: {odd}")
    