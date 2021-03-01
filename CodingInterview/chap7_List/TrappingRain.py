#TrappingRain

import sys
from typing import List
sys.stdin = open('input/TrappingRain')

def my(heights:List[int])->int:
    left = 0
    n = len(heights)
    while heights[left]==0:
        left+=1
    right=left+1
    answer =0
    while right < n-1:
        while left <n-1 and right < n-1 and heights[left] > heights[right]:
            right+=1
            if right ==n-1:
                left+=1
                right=left+1
        height = min(heights[left],heights[right])
        width = right-left+1
        water = height*width - sum(heights[left:right])-heights[left]
        print(water,left,right)
        left=right
        right+=1
        answer+=water
    return answer

def two_point(height:List[int])->int:
    if not height:
        return 0
    volume =0
    left,right = 0, len(height)-1
    left_max,right_max=height[left],height[right]
    while left<right:
        left_max, right_max = max(height[left],left_max),max(height[right],right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max<= right_max:
            volume+=left_max-height[left]
            left+=1
        else:
            volume +=right_max-height[right]
            right -=1
    return volume

def with_stack(height:List[int])->int:
    stack = []
    volume = 0
    for i in range(len(height)):
        #변곡점을 만나는 경우
        while stack and height[i]>height[stack[-1]]:
            #스택에서 꺼낸다
            top = stack.pop()
            if not len(stack):
                break
            #이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1]-1
            waters = min(height[i],height[stack[-1]])-height[top]
            volume+=distance*waters
        stack.append(i)
    return volume

heights = list(map(int,input().split()))
print(my(heights))