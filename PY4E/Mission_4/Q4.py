import re

p = re.compile('\d{2}([0]\d|[1][0-2])([0][1-9]|[1-2]\d|[3][0-1])[-]*[1-4]\d{6}')

def check_num(num):
    gender =  num[7]
    year = num[0:2]
    month = num[2:4]
    if 0<=int(year)<=21:
        answer = input("2000년 이후 출생자입니까? 맞으면 o 틀리면 x :")
        if answer =='x':
            print('잘못된 번호입니다.')
            print('올바른 번호를 넣어주세요.')
            return

    gender = '남자' if gender == '1' or gender == '3' else '여자'
    print(f'{year}년 {month}월 {gender}')


while True:
    num = input("주민등록번호를 입력하세요 xxxxxx-xxxxxxx:")
    if re.match(p,num):
        check_num(num)
        break
    print('잘못된 입력입니다.')
