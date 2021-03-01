#snail

# 5*5

list = [[0]*5 for i in range(5)]
max = len(list[0])
d =1
x=0
y=-1
cnt=1
while max>0:
    for i in range(max):
        y+=d
        list[x][y]=cnt
        cnt+=1
    max-=1
    for i in range(max):

        x+=d
        list[x][y]=cnt
        cnt+=1
    d=d*-1
print(list)

