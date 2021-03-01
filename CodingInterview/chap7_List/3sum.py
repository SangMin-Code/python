import sys
from typing import List

sys.stdin = open('input/3sum')


def my(nums:List[int])->List[List[int]]:
    answer = []
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if j == i :
                continue
            for k in range(n) :
                if k==j or k ==i :
                    continue
                if nums[i]+nums[j]+nums[k] == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    if sorted(temp) not in answer:
                        answer.append(sorted(temp))
    print(answer)

def three_sum(nums:List[int])->List[List[int]]:
    results =[]
    nums.sort()
    #브루트포스 n^3 반복
    for i in range(len(nums)-2):
        #중복된 값 건너뛰기
        if i >0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k>j+1 and nums[k]==nums[k-1]:
                    continue
                if nums[i]+nums[j]+nums[k]==0:
                    results.append((nums[i],nums[j],nums[k]))
    return results

def using_two_point(nums:List[int])->List[List[int]]:
    results =[]
    nums.sort()

    for i in range(len(nums)-2):
        #중복된 값 건너뛰기
        if i>0 and nums[i]==nums[i-1]:
            continue

        #간격을 좁혀가며 합 sum 계산
        left, right = i+1, len(nums)-1
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum<0:
                left+=1
            elif sum>0:
                right-=1
            else:
                #sum=0 인 경우이므로 정답 및 스킵 차리
                results.append(nums[i],nums[left],nums[right])

                while left < right and nums[left] ==nums[left+1]:
                    left +=1
                while left < right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1

nums = list(map(int,input().split()))
#my(nums)
print(three_sum(nums))