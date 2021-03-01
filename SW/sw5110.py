# sw5110.py

import sys
sys.stdin = open("/SW/input/sample_input.txt", "r")
'''
[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.
'''
'''
TC = int(input())
for test_case in range(1,TC+1):
    N,M = map(int,input().split())
    resultList = list(map(int,input().split()))
    #print(resultList)
    for i in range(M-1):
        tempList = list(map(int,input().split()))
        a = tempList[0]
        if max(resultList) > a:
            for j in range(len(resultList)):
                if resultList[j]>a  :
                    idx = j
                    break
            resultList = resultList[:idx]+tempList+resultList[idx:]
        else:
            resultList.extend(tempList)
        #print(f'input: {tempList} ## result: {resultList} ## idx :{idx}')
    answer = [resultList[i] for i in range(len(resultList)-1,len(resultList)-11, -1)]
    print(f'#{test_case}',end=' ')
    print(*answer[:])
'''
def mergeSeqLists():
    first_seq = list(map(int, input().split()))
    for _ in range(M - 1):
        seq_len = len(first_seq)
        next_seq = list(map(int, input().split()))
        for i in range(seq_len):
            if first_seq[i] > next_seq[0]:
                first_seq[i:0] = next_seq
                break
        if seq_len == len(first_seq):
            first_seq.extend(next_seq)
        print(first_seq)
    return first_seq


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    ans = mergeSeqLists()

    print('#{} '.format(test_case), end='')
    print(' '.join(str(n) for n in ans[-1:-11:-1]))
'''
#1 16 15 10 9 5 6 7 8 4 4
#2 251 798 365 506 494 193 675 387 334 224
#3 404 483 16 788 123 274 231 659 778 178	 
'''