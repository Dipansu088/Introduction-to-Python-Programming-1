# Count vowels and consonants in a string.

s=input("Enter string: ").strip()
vowel=0
consonant=0

for i in s.lower():
    if i in 'aeiou':
        vowel+=1
    else:
        consonant+=1
        
print(vowel, consonant)