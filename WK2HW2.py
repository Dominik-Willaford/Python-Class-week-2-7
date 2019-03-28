num = int
num = 1
squareNum = int
cubeNum = int
fourthNum = int

print('Welcome to your calculator')
while (num < 11): 
    squareNum = num * num
    cubeNum = squareNum * num
    fourthNum = cubeNum * num
    print(num,"\t", squareNum,"\t", cubeNum,"\t", fourthNum)
    num = num + 1
