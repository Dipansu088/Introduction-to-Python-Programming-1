# Write a Python program to reverse each word in a sentence while keeping the original order of the words.
# Eg: Input: Python is interesting
# Outout: nohtyP si gnitseretni

def reverse_words(s):
    words=s.split()
    result=""
    for word in words:
        result=result+word[::-1]+" "
    return result

s=input("Enter a sentence: ")
print(reverse_words(s))