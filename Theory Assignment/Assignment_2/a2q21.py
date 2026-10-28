# Consider the list L1=[“C+=”,“Python”, java”,”python”,”SQL”, “Java”]. Find the unique words present in the list, ignoring the case.

L1 = ["C+=", "Python", "java", "python", "SQL", "Java"]

result=[]

# unique=set()

# for i in L1:
#     unique.add(i.lower())
# print(unique)

for i in L1:
    if i.lower() not in result:
        result.append(i.lower())
print(result)