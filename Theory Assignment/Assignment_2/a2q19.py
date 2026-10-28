# Develop a python function that takes a string as parameter and returns a string with every successive repetitive character replaced with a star (#). For example, „committee‟ will be returned as „com#it#e#‟.

s=input("Enter a string: ")
s2=s[0]
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        s2=s2+'#'
    else:
        s2=s2+s[i]

print(s2)