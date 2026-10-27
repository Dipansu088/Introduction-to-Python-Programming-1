# Write a function in python that takes a sentence as an input parameter and displays the number of words starting with a vowel in the sentence.

def countVowelWords(s):
    count=0
    words=s.split()
    for i in words:
        if i[0] in 'aeiou':
            count+=1
    return count

s=input("Enter a sentence: ").strip().lower()
print(countVowelWords(s))