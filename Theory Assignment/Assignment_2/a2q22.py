# Initialize two sets and, find the elements that appear in exactly one set but not both. (Hint: Use symmetric difference)

s1={1,2,3,4,5}
s2={5,2,7,1,8}

result=s1.symmetric_difference(s2)
print(result)