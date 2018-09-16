import math

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascals_triangle(rows):
    result = []
    for i in range(rows):
        row = []
        for j in range(i + 1):
            row.append(combination(i, j))
        result.append(row)
    return result

num = int(input('enter: '))

for row in pascals_triangle(num):
    print(row)
