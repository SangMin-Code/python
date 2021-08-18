import collections
import random
from typing import List


def guess_number():
    min_num, mid_num, max_num = map(str,makeThreeNum())
    dic = [[min_num,'최솟값'],[mid_num,'중간값'],[max_num,'최댓값']]

    try_num = 0
    try_list= []

    while True:

        if not dic:
            print('게임 종료')
            print(f'{try_num}번 시도만에 예측 성공')
            break

        try_num += 1
        print(f'{try_num}차 시도')
        while True:
            input_num = input_check(input('숫자를 예측해보세요 : '))
            if input_num in try_list:
                print('이미 예측에 사용한 숫자입니다.')
                continue
            if input_num !='-1':
                break

        try_list.append(input_num)
        if input_num not in [i[0] for i in dic]:
            print(f'{input_num}는 없습니다.')
            hint(input_num,dic,try_num)
        else :
            for i in dic:
                if i[0]==input_num:
                    print(f'숫자를 맞추셨습니다! {input_num}은/는 {i[1]}입니다')
                    dic.remove(i)
                    break




def hint(input_num:str, last_dic:List[List[str]],try_num:int):
    if try_num<5:
        return

    input_num = int(input_num)
    min_num,min_name = int(last_dic[0][0]),last_dic[0][1]
    max_num,max_name = int(last_dic[-1][0]),last_dic[-1][1]

    if abs(input_num-min_num) <= abs(input_num-max_num):
        if input_num > min_num:
            print(f'{min_name}은 {input_num} 보다 작습니다.')
        else :
            print(f'{min_name}은 {input_num} 보다 큽니다.')
    else :
        if input_num > max_num:
            print(f'{max_name}은 {input_num} 보다 작습니다.')
        else :
            print(f'{max_name}은 {input_num} 보다 큽니다.')


def input_check(s:str):
    if s.isdecimal() and 100>=int(s)>=0:
        return s
    else :
        print('0 ~100 숫자를 입력해주세요')
        return '-1'

def makeThreeNum()->List[int]:
    numList = []
    while len(numList)<3:
        number=random.randint(0,100)
        if number not in numList:
            numList.append(number)

    return sorted(numList)


guess_number()