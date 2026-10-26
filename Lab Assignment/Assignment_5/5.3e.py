# Check if a string contains at least one digit and one alphabet.

def chk_string(s):
    has_digit=False
    has_alpha=False
    
    for ch in s:
        if ch.isdigit():
            has_digit=True
        if ch.isalpha():
            has_alpha=True
    
    if has_digit and has_alpha:
        return "It has"
    else:
        return "No"
    
s=input("Enter a string: ")
print(chk_string(s))