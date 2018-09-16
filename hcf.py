def hcfify(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            hcf = i

    return hcf

num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))

print("The hcf of", num1,"and", num2,"is", hcfify(num1, num2))
