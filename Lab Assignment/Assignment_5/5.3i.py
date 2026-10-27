# Reverse a string without reversing the words. Example:
# input : ‘hello students’
# output: ‘students hello’

def reverse_string(s):
    words=s.split()
    words.reverse()
    
    result=" ".join(words)
    return result

s=input("Enter a string: ")
print(reverse_string(s))