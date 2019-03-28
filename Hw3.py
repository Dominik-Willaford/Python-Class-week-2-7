a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6,7,8,9]

result = [b*a for a,b in zip(b,a)]
print(result)
