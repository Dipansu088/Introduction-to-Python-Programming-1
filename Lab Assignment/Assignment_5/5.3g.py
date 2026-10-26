# Count frequency of characters in a string.

def calc_freq(s):
    frq={}
    for ch in s:
        if ch in frq:
            frq[ch]=frq[ch]+1
        else:
            frq[ch]=1
            
    return frq

s=input("Enter the string: ")
print(calc_freq(s))