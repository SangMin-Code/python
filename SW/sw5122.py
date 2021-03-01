#sw5120.py
'''
3
5 3 4
1 2 3 4 5
I 2 7
D 4
C 3 8
5 5 2

I 2 7 -> 2번 인덱스 앞에 7을 추가하고, 한 칸 씩 뒤로 이동한다.
D 4 -> 4번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동한다.
C 3 8 -> 3번 인덱스 자리를 8로 바꾼다.
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.

그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M
'''

import sys
sys.stdin = open("/input/sample_input.txt", "r")
TC = int(input())
for test_case in range(1,TC+1):
    N,M,L = map(int,input().split())
    nList = list(map(int,input().split()))
    for i in range(M):
        t = list(input().split())
        if 'I' in t :
            idx,num = int(t[1]),int(t[2])
            nList.insert(idx,num)
        elif 'D' in t:
            idx = int(t[1])
            nList.pop(idx)
        elif 'C' in t:
            idx,num = int(t[1]),int(t[2])
            nList[idx]=num
    if L>len(nList)-1:
        answer =-1
    else :
        answer = nList[L]
    print(answer)
'''
#1 5
#2 10239
#3 -1	 
'''