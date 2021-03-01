import sys
sys.stdin = open('input/samenumber')
nList = list(map(int,input().split()))
stack = []
stack.append(nList[0])
for i in range(1,len(nList),1):
    #print(nList[i])
    if stack[-1]==nList[i]:
        stack.pop(-1)
    else :
        stack.append(nList[i])
print(stack)

