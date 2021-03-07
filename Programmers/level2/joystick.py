#https://programmers.co.kr/learn/courses/30/lessons/42860
import sys
sys.stdin = open('input/joystick')

def my(in_str :str)->int:
    list = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in in_str]
    idx = 0
    answer = 0
    while True:
        answer+=list[idx]
        list[idx]=0
        if sum(list)==0:
            return answer
        left, right = 1,1 # 좌 우 중 바꿀 수 있는 가장 짧은 방향
        while list[idx-left]==0:
            left+=1
        while list[idx+right]==0:
            right+=1
        answer+=left if left<right else right
        idx += -left if left<right else right

def pracice(in_str : str)->int:
    list = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in in_str]
    idx = 0
    answer=0
    while True:
        answer+=list[idx]
        list[idx]=0
        if sum(list)==0:
            return answer
        left,right=1,1
        while list[idx-left]==0:
            left+=1
        while list[idx+right]==0:
            right+=1
        answer += left if left<right else right
        idx += -left if left<right else right

TC = int(input())
for test_case in range(1,TC+1):
    str = input()
    answer = my(str)
    print(answer)