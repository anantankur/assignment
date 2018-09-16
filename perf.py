num = int(input('enter number: '))
sum = 0
for x in range(1, num):
    if num % x == 0:
        sum += x

if sum==num:
    print('perfect no.')
else:
    print('not perfect')
