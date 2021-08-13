user = input()
head, tail = user.split('-')[0], user.split('-')[1]
if tail[0] == '1' or tail[0] == '3':
    print('남자입니다')
elif tail[0] == '2' or tail[0] == '4':
    print('여자입니다')