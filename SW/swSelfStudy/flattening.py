#flattening

import  sys
sys.stdin=open("input/flattening", "r")

N = int(input())
nlist = list(map(int, input().split()))
print(nlist)
answer = -1
for i in range(N):
    maxVal = max(nlist)
    minVal = min(nlist)
    maxidx = nlist.index(maxVal)
    minidx = nlist.index(minVal)
    nlist[maxidx]=nlist[maxidx]-1
    nlist[minidx]=nlist[minidx]+1
answer = max(nlist)-min(nlist)
print(nlist)