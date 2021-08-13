
user = input()
user_num = list(map(int,user))
print(user_num)

count =2
total=0
for num in user_num[:-1]:
    if count>=10:
        count =2
    total = total + num*count #주민번호 끝자리는 0이 될 수 없다.
    print(f'{total} = {total} + {num}*{count}')
    count = count +1

istrue = 11 - (total % 11)
print(user_num[:-1][0],type(user_num[:-1][0]),type(istrue))
print(istrue == user_num[-1])
if istrue == user_num[-1]:
    print('올바른 주민등록번호 입니다')
else:
    print('올바르지 않은 주민등록번호')

print(istrue, user_num[-1])

