user = input()
tail = user.split('-')[1]
print("hi")
if tail[0:2] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
    print('seoul 입니다')
else:
    print('seoul이 아닙니다')