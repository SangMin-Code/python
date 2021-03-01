#sw5120.py
'''
3
6 3 3
6 2 4 9 1 5
5 3 5
958 386 329 169 778
10 4 10
158 606 636 941 686 774 302 375 954 668

- 1000이하의 숫자 N개가 주어진다. 이때 시작 숫자가 정해지고, 첫 번째 지정 위치가 된다.

- 지정 위치부터 M번째 칸을 추가한다. 여기에 앞칸의 숫자와 뒤로 밀려난 칸의 숫자를 더해 넣는다. 추가된 칸이 새로운 지정 위치가 된다. 밀려난 칸이 없으면 시작 숫자와 더한다.

- 이 작업을 K회 반복하는데, M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터 이어간다.

- 마지막 숫자부터 역순으로 숫자를 출력하면 비밀번호가 된다. 숫자가 10개 이상인 경우 10개까지만 출력한다.
'''

import sys
sys.stdin = open("/input/sample_input.txt", "r")
TC = int(input())
for test_case in range(1,TC+1):
    N,M,K = map(int,input().split())
    pw=list(map(int,input().split()))
    idx = 0
    for i in range(K):
        idx = idx +M
        if idx > len(pw):
            idx = idx - len(pw)
        if idx == len(pw) :
            a,b=pw[0],pw[len(pw)-1]
            pw.append(a+b)
        else :
            a,b = pw[idx-1],pw[idx]
            pw.insert(idx,a+b)
        #print(f'idx :{idx} , pw :{pw}')
    if len(pw)>10:
        answer = [pw[i] for i in range(len(pw)-1,len(pw)-11,-1)]
    else :
        answer = [pw[i] for i in range(len(pw)-1,-1,-1)]

    print(f'#{test_case} {answer}')

'''
#1 5 6 1 9 13 4 2 8 6
#2 1736 2514 778 169 667 498 329 715 386 958
#3 826 1494 668 954 375 1052 677 302 774 2234	 
'''