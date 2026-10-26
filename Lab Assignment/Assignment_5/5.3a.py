# Check if a string is symmetric or asymmetric.

def chk_sym(txt):
    mid=len(txt)//2
    
    first_half=txt[:mid]
    second_half=txt[mid:]
    
    if first_half==second_half:
        return "Symmetric"
    else:
        return "Asymmetric"
    
txt=input("Enter a text: ").lower()
print(chk_sym(txt))