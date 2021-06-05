# 14426.py
import sys
from typing import List

sys.stdin = open('input/14426')


n, m = map(int, sys.stdin.readline().rstrip().split())
strings = [sys.stdin.readline().rstrip() for _ in range(n)]
cnt = 0

for _ in range(m):
    pattern = sys.stdin.readline().rstrip()
    for s in strings:
        if pattern == s[:len(pattern)]:
            cnt += 1
            break
print(cnt)

