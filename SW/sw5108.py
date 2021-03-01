# sw5108.py

import sys
sys.stdin = open("/input/sample_input.txt", "r")
'''
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.

그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M
'''

TC = int(input())
for test_case in range(1, TC+1):
    N,M,L = map(int,input().split())
    numList = list(map(int,input().split()))
    for i in range(M):
        idx, num = map(int,input().split())
        numList.insert(idx,num)
    print(f'#{test_case} {numList[L]}')