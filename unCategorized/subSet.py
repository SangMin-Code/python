arr = [1,2,3,4,5,6,7,8,9,10,11,12]

N = 3
K = 10
cnt =0
n = len(arr)
subSet =[]
for i in range(1<<n):
    temp = []
    for j in range(n):
        if i &(1<<j):
            temp.append(arr[j])
    subSet.append(temp)




for i in range (len(subSet)):
    if len(subSet[i]) == N:
        sum =0
        for j in range(len(subSet[i])):
            sum += subSet[i][j]
        if sum == K : cnt +=1
print(cnt)
