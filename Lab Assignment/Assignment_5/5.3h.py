# Find the character having maximum frequency in a string.

def count_maxfrq(s):
    frq={}
    for ch in s:
        if ch in frq:
            frq[ch]=frq[ch]+1
        else:
            frq[ch]=1
            
    max_char=""
    max_count=0
    
    for ch in frq:
        if frq[ch]>max_count:
            max_count=frq[ch]
            max_char=ch
            
    return max_char

s=input("Enter string: ")
print("Maximum frq ch:",count_maxfrq(s))