# Write a Python program to calculate tax on the basis of conditions given below cost in rupees using an if-elif-else statement.
# Cost in Rs
# Tax
# >100000
# 15%
# >50000 and <=100000
# 10%
# <=50000
# 5%

cost=float(input("Enter cost: "))
if cost>100000:
    tax=cost*15/100
elif cost>50000 and cost<=100000:
    tax=cost*10/100
elif cost<=50000:
    tax=cost*5/100
else:
    print("Enter valid cost")
    
print(tax)