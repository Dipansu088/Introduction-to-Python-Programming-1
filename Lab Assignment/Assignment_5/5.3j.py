# Counting the Number of Common Characters in a Pair of Strings

def count_com(s1,s2):
    count=0
    for ch in s1:
        if ch in s2:
            count+=1
    return count

s1=input("Enter a string: ")
s2=input("Enter another string: ")
print(count_com(s1,s2))