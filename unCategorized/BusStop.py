#BusStop.py

index = 0
flag = False
location = 0
cnt = 0

k = 10
n = 12
numList = [1,3,5,8]

while(True):
    index = location
    if index+k >=n :break
    else :
        for i in range(0,3):
            if index+k-i in numList :
                cnt += 1
                flag = True
                location = index+k-i
                break
        if flag ==False :
            cnt =0
            break
    flag = False
print(f"cnt : {cnt}")