num = int(input("enter: "))

leng = len(str(num))
sum = 0
trash = num

while(trash != 0):
    sum = sum + ((trash % 10) ** leng)
    trash = trash // 10

if sum == num:
    print("armstrong number")
else:
    print("not armstrong number")
