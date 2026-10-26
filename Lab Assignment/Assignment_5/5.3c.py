# Given a string s and index i, delete ith value from s.

def delete_ch(txt,i):
    if i<0 or i>=len(txt):
        return "Invalid"
    result=txt[:i]+txt[i+1:]
    return result

txt=input("Enter a string: ")
i=int(input("Enter index: "))
print(delete_ch(txt, i))