# Write the following code using list comprehension:
# (i) numbers = [2, 3, 6, 7, 9, 10, 12]
# result = []
# for x in numbers:
# if x % 3 == 0:
# result.append(x ** 3)
# print(result)
# (ii) numbers = [1, 2, 3, 4, 5]
# result = []
# for x in numbers:
# if x % 2 == 0:
# result.append("Even")
# else:
# result.append("Odd")
# print(result)

#i

numbers = [2, 3, 6, 7, 9, 10, 12]
result=[x**3 for x in numbers if x%3==0]
print(result)

#ii

num = [1, 2, 3, 4, 5]
result=["Even" if x%2==0 else "Odd" for x in num ]
print(result)