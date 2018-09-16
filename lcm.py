def lcmify(num1, num2):
   if num1 > num2:
       greater = num1
   else:
       greater = num2

   while(True):
       if((greater % num1 == 0) and (greater % num2 == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input('num1: '))
num2 = int(input('num2: '))

print("The lcm of","is", lcmify(num1, num2))
