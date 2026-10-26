# Check if a string is palindrome.

def chk_pallindrome(t):
    reverse=t[::-1]
    if t==reverse:
        return "Pallindrome"
    else:
        return "Not pallindrome"

t=input("Enter a text: ")
print(chk_pallindrome(t))