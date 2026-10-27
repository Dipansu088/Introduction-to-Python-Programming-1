# Write a Python program to input a string and remove repeated characters from a string without changing the order of the remaining characters.
# Eg: Input: programming
# Output: progamin

def remove_duplicates(s):
    result=""
    for ch in s:
        if ch not in result:
            result=result+ch
    return result

s=input("Enter the string: ")
print(remove_duplicates(s))