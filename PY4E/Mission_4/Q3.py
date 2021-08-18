import os.path
import re
def guest_book() :
    p = re.compile('010-\d{4}-\d{4}')

    f= open(f'storage/방명록.txt', 'w',encoding='utf8')

    print('방명록을 입력해주세요 : ')
    lines =[]
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    uncorrect_member = []

    for line in lines:
        f.write(line+'\n')
        if not re.match(p,line.split(',')[1]):
            uncorrect_member.append(line)
    f.close()

    for guest in uncorrect_member:
        name,phone = guest.split(',')
        print(f'잘못 쓴 사람 : {name}')
        print(f'잘못 쓴 번호 : {phone}\n')

guest_book()