#gravity

'''
첫번째줄에test  case의수T(1≤T≤100)가주어진다.
각케이스의첫째줄에방의가로길이N(2≤N≤100)과방의세로길이M(2≤M≤100)이주어진다.
 다음줄에는N개의상자들이쌓여있는높이H(0≤H≤M)가주어진
'''

import sys
sys.stdin = open("input/gravity", "r")

TC = int(input())
for test_case in range(1,TC+1):
    N,M = map(int, input().split())
    vList = list(map(int,input().split()))
    maxVal = max(vList)
    maxList =[]
    result = 0
    for i in range(len(vList)):
        if vList[i]==maxVal:
            maxList.append(i)

    if len(vList) == 1 :
        result = N-(maxList[0]+1)
    else :
        result = N-(maxList[-1])
        for i in range(len(maxList)-1):
            if result < maxList[i+1]-maxList[i]:
                result = maxList[i+1]-maxList[i]
    print(result)

