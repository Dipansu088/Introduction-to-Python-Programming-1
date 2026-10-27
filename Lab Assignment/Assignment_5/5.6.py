# Write a function in python that takes a sentence as an input parameter and replaces the first letter of every word with the corresponding uppercase letter and rest of the letters in the word by corresponding letters in lowercase without using built-in function.

def change_case(s):
    words=s.split()
    result=""
    
    for word in words:
        first=word[0]
        
        if 'a' <= first <= 'z':
            first=chr(ord(first)-32)
        result+=first
        
        for ch in word[1:]:
            if 'A' <= ch <= 'Z':
                ch=chr(ord(ch)+32)
            result+=ch
        result+=" "
        
    return result

s=input("Enter a sentence: ")
print(change_case(s))