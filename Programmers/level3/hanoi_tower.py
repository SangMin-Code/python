#hanoi_tower
import sys
sys.stdin=open('input/hanoi_tower')
from typing import List


def move(frm, to, mid, n, answer):
    if n == 1:
        # 시작지 -> 목적지를 answer에 리스트로 저장한다
        answer.append([frm, to])
        return
    # 1.
    move(frm, mid, to, n - 1, answer)
    # 2.
    answer.append([frm, to])
    # 3.
    move(mid, to, frm, n - 1, answer)

def my(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer

TC = int(input())
for test_case in range(1,TC+1):
    n= int(input())
    answer = my(n)
    print(answer)