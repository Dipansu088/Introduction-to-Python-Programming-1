'''Write a function in python that takes a string as a parameter and returns a string with every successive repetitive character replaced with a star(*). For example, ‘hello’ is returned as ‘he**o’.'''

def replace_rep(text):
    result=""
    for i in range(len(text)):
        if ((i>0 and text[i]==text[i-1]) or (i<len(text)-1 and text[i]==text[i+1])):
            result=result+"*"
        else:
            result=result+text[i]
            
    return result

txt=input("Enter a text: ")
print(replace_rep(txt))