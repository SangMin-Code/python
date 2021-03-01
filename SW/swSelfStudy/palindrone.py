#palindrone

import sys
sys.stdin=open('input/palindrone', 'r')

n = int(input())
sList=[]
for i in range(8):
    sList.append(input())
temp = []
for i in range(8):
    s=''
    for j in range(8):
        s+=sList[j][i]
    temp.append(s)
sList.extend(temp)

answer =0
for i in range(len(sList)): #list
    for j in range(8-n+1): # list[i]의 첫4글자부터
            flag = True
            for k in range(2):
                if sList[i][j+k] != sList[i][j+n-k-1]:
                    flag = False
                    break
            if flag : answer +=1
print(answer)
