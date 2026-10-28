# Write a python program that takes the x – y coordinates of a point in the Cartesian plane and prints a message telling either an axis on which the point lies or the quadrant in which it is found.

print("Enter both x and y coordinates below: ")
x=float(input())
y=float(input())

if x>0 and y>0:
    print("Q1")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
elif x>0 and y<0:
    print("Q4")
elif x==0 and y==0:
    print("Origin")
elif x==0:
    print("Y axis")
else:
    print("X axis")
