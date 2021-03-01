#circulation.py

import sys
sys.stdin = open("/input/sample_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    n,c = map(int, input().split())
    nlist = list(map(int,input().split()))

    for i in range(c):
        temp = nlist.pop(0)
        nlist.append(temp)
    answer = nlist[0]
    print(f'#{test_case} {answer}')

