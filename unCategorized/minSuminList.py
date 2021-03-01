#minSuminList.py

'''
2 1 2
5 8 5
7 2 2
'''
import sys
sys.stdin = open("/input/sample_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nlist = list(map(int,input().split()))

    #print(f'#{test_case} {answer}')