# Remove duplicates from a string.

def remove_dup(s):
    result=""
    for i in s:
        if i not in result:
            result=result+i
            
    return result

s=input("Enter a string: ")
print(remove_dup(s))