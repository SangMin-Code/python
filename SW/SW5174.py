# SW5174

'''
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.

노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

import sys

sys.stdin = open("/SW/input/sample_input.txt", "r")
def find(n):
    global  cnt
    cnt+=1
    for i in eList[n]:
        find(i)
    return

def find2(n):
    sum =0
    for i in eList[n]:
        sum+=find2(i)
    if not eList[n] :
        return 1
    else :
        return sum+1



TC = int(input())
for test_case in range(1,TC+1):
    E,N = map(int,input().split())
    eList = [ [] for i in range(E+2)]
    t = list(map(int,input().split()))
    for i in range(E):
        eList[t[2*i]].append(t[2*i+1])
    #cnt = 0
    #find(N)
    answer =find2(N)
    print(answer)


'''
#1 3
#2 1
#3 3
'''