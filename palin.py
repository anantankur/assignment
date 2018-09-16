n = int(input('enter: '))

str_n = str(n)

leng = len(str_n)

rev_list = []

rev_int_str = ''

for i in range(leng):
    rev_list.append(str_n[leng-i-1])

rev_int_str = rev_int_str.join(rev_list)

rev_int = int(rev_int_str)

def p_check(num):
    if num == rev_int:
        print('palindrome')
    else:
        print('not')


p_check(n)
