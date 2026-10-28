# Write a program to find all twin prime pairs between 1 and 100.
# Ex: (3, 5)
# (5, 7)
# (11, 13)
# (17, 19)

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
for n in range(2,99):
    if is_prime(n) and is_prime(n+2):
        print(n,",",n+2)