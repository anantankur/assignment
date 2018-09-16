def perfect_number(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum += x
    return(sum == num)

num = int(input('enter number: '))

print(perfect_number(num))
