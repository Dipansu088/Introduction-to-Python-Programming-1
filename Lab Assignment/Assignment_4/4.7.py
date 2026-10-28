# Write a python program to check whether the input 3 digit number is a perfect number or
# not. A perfect number is a positive whole number that equals the sum of its positive divisors excluding the number itself. Ex: 6=1+2+3

n=int(input('Enter a 3 digit number: '))
if n>99 and n<1000:
    sumofdivisor=0
    for i in range(1,n//2+1):
        if n%i==0:
            sumofdivisor+=i
    if sumofdivisor==n:
        print("Perfect")
    else:
        print("Not a perfect")
else:
    print("Enter a 3 digit no.")