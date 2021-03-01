#binarySearch

# 페이지,  찾을 페이지 1, 찾을 페이지 2
r =1000
p1 = 299
p2 = 578
lp = 0
p = [p1,p2]
cntList = []
for i in p:
    cnt = 0
    lp = 1
    rp = r
    while(lp<=rp):
        cp = (lp+rp)//2
        print(lp,cp,rp)
        if cp == i :
            break
        elif cp > i :
             rp = cp-1
             cnt +=1
        elif cp < i :
             lp = cp+1
             cnt +=1
    cntList.append(cnt)
if cntList[0]-cntList[1]<0:print("A")
elif cntList[0]-cntList[1]==0 : print(0)
else : print("B")
print(cntList[0],cntList[1])