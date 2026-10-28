# Develop a Python program that inputs a string and identifies the character occurring most frequently in a given string and displays its frequency.

s=input("Enter a string: ")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

max_chr=""
max_count=0

for ch in freq:
    if freq[ch]>max_count:
        max_count=freq[ch]
        max_chr=ch
print("most freq ch:",max_chr)
print("frequency:",max_count)