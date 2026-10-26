# Count the number of vowels and consonants in a string.

def count_vc(s):
    consonants=0
    vowels=0
    for i in s:
        if i in "aeiou":
            vowels+=1
        else:
            consonants+=1
    return vowels, consonants

s=input("Enter a string: ").lower().strip()
print(f"Vowels and consonants= {count_vc(s)}")