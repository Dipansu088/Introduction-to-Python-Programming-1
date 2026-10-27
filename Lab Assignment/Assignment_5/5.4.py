# Write a function in python that takes a string as an input and determines the count of the number of words.

def count_words(s):
    words=s.split()
    return len(words)

s=input("Enter a string: ")
print(count_words(s))