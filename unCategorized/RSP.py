#RSP.py

import sys
sys.stdin = open("/input/sample_input.txt", "r")

def RSP(l,r,list):
    cp = (l+r)//2
    #print(l,cp,r)
    if r-l>=2 :
        l = RSP(l,cp,list)
        r = RSP(cp+1,r,list)
    val =list[l]-list[r]
    if val ==2 : return r
    elif val == -2 : return l
    elif val >=0 : return l
    else : return r
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nlist = list(map(int,input().split()))
    answer =RSP(0,n-1,nlist)+1
    print(f'#{test_case} {answer}')