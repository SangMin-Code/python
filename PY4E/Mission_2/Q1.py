import random

def check(s):
    if s=='0' or s=='1' or s=='2':
        s = int(s)
    elif s=='가위':
        s = 0
    elif s=='바위':
        s = 1
    elif s=='보':
        s = 2
    else:
        return -1
    return s

def print_rcp(who,rcp):
    s = ''
    if rcp==0:
        s='가위'
    elif rcp==1:
        s='바위'
    else:
        s='보'
    print(f'{who}:{s}')

def rcp(my:str):

    #입력값 체크
    val = check(my)
    if val== -1:
        print('0,1,2,가위,바위,보 중에 입력해주세요.')
        return

    computer = random.randint(0,2)

    print_rcp('나',val)
    print_rcp('컴퓨터',computer)

    if val==computer:
        print('비겼습니다!')

    if val==0:
        if computer==1:
            print('컴퓨터 승리!')
        elif computer==2:
            print('나 승리!')
    elif val==1:
        if computer==2:
            print('컴퓨터 승리!')
        elif computer==0:
            print('나 승리!')
    else:
        if computer==0:
            print('컴퓨터 승리!')
        elif computer==1:
            print('나 승리!')


my = input("가위 바위 보 : ")
rcp(my)







