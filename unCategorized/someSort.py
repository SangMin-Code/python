#someSort

nList = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(nList)):
    for j in range(i+1, len(nList)):
        if i%2==0 and nList[j]>nList[i]:
            nList[i],nList[j]=nList[j],nList[i]
        elif i%2!=0 and nList[j]<nList[i]:
            nList[i],nList[j]=nList[j],nList[i]
print(f"#{nList}")