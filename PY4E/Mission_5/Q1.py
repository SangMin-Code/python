import re
import random

TARGET_NUMBER = 31


def game():
    current_num = 0
    while True:
        while True:
            current_num = input_my(current_num+1)
            if current_num:
                break
        if current_num >= TARGET_NUMBER:
            print('you lose!')
            break
        current_num = input_com(current_num+1)
        if current_num >= TARGET_NUMBER:
            print('you lose!')
            break


def input_com(n):
    input_com = random.randint(0,2)
    print('컴퓨터 : ', end="")
    for i in range(n,n+input_com+1):
        print(f'{i}', end=" ")
    print()
    print(f'현재 숫자 : {input_com+n}')
    return input_com+n


def input_my(n):
    my_turn = ''
    while True:
        my_turn =input(f'My turn _ {n} 이상 숫자를 입력해세요(ex 1 2 3) : ')
        next_num = isNum(my_turn,n)
        if next_num:
            return next_num


def isNum(str,n):

    numList = str.split()

    if len(numList)>3 or len(numList)==0:
        print('1개~3개의 숫자를 입력해주세요.')
        return 0

    try :
        numList = [int(i) for i in numList]
    except ValueError:
        print('숫자를 공백으로 구분지어 입력해주세요.')
        return 0

    if numList[0] != n:
        print(f'{n}부터 시작해주세요')
        return 0

    for i,num in enumerate(numList):
        if i>0 and int(numList[i]) != int(numList[i-1])+1:
            print('연속된 숫자를 입력해주세요.')
            return 0

    print(f'현재 숫자 : {numList[-1]}')

    return numList[-1]


game()
