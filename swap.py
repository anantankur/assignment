num = int(input('enter number: '))

strNum = str(num)

lister = list(strNum)

lister[0], lister[-1] = lister[-1], lister[0]

strNum = ''.join(lister)

print(int(strNum))
