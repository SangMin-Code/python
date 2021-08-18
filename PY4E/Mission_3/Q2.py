import random
def rsp_advanced(games:int):

    my,com = -1,-1
    my_win,draw = 0,0

    for i in range(1,games+1):
        my,com = input_rsp(),random.randint(0,2)

        if my==0:
            print('나:가위')
            if com==2:
                print('컴퓨터:보')
                print(f'{i}번째 판 나의 승리!')
                my_win+=1
            elif com==1:
                print('컴퓨터:바위')
                print(f'{i}번째 판 컴퓨터의 승리!')
            else:
                print('컴퓨터:가위')
                print(f'{i}번째 판 비겼습니다!')
                draw+=1
        elif my==1:
            print('나:바위')
            if com==0:
                print('컴퓨터:가위')
                print(f'{i}번째 판 나의 승리!')
                my_win+=1
            elif com==2:
                print('컴퓨터:보')
                print(f'{i}번째 판 컴퓨터의 승리!')
            else:
                print('컴퓨터:바위')
                print(f'{i}번째 판 비겼습니다!')
                draw+=1
        else:
            print('나:보')
            if com==1:
                print('컴퓨터:바위')
                print(f'{i}번째 판 나의 승리!')
                my_win+=1
            elif com==0:
                print('컴퓨터:가위')
                print(f'{i}번째 판 컴퓨터의 승리!')
            else:
                print('컴퓨터:보')
                print(f'{i}번째 판 비겼습니다!')
                draw+=1
    my_lose = games-my_win-draw
    print(f'나의 전적 : {my_win}승 {draw}무 {my_lose}패')
    print(f'컴퓨터의 전적 :{my_lose}승 {draw}무 {my_win}패 ')

def input_rsp()->int:
    while True:
        rsp = input("0.가위 1.바위 2.보 :").strip()
        if rsp=='0' or rsp=='가위':
            return 0
        elif rsp=='1' or rsp=='바위':
            return 1
        elif rsp=='2' or rsp =='보':
            return 2
        else:
            print('0,1,2,가위,바위,보 중에 입력해주세요.')

while True:
    games = input("몇 판을 진행하시겠습니까? :")
    if not games.isdecimal() or not int(games)>0:
        print('유효한 1 이상의 숫자가 아닙니다.')
    else :
        games = int(games)
        break

rsp_advanced(games)