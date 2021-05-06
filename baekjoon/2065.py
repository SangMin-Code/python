# 2065.py
import sys
from typing import List

sys.stdin = open('input/2065')
import collections

# def my(M:int, t:int, N:int, customers:List[int])->List[int]:
#     current_time = 0
#     left_customers = collections.deque()
#     right_customers = collections.deque()
#     answer =[-1]*N
#     for idx,customer in enumerate(customers):
#         if customer[1]=="left":
#             left_customers.append([int(customer[0]),idx])
#         else :
#             right_customers.append([int(customer[0]),idx])
#
#     p_dic = {"left":"right","right":"left"}
#     c_dic = {"left":left_customers,"right":right_customers}
#     position = "left"
#
#     while len(left_customers)>0 or len(right_customers)>0:
#         current_customers = c_dic[position]
#
#         c_cnt = 0
#         c_flag = False
#
#         #도착한 곳에서 손님을 태우기
#         while current_customers and int(current_customers[0][0])<=current_time\
#             and c_cnt<M:
#             pop_customer= current_customers.popleft()
#             answer[pop_customer[1]] =current_time+t
#             c_flag=True
#             c_cnt+=1
#
#         #손님을 태울 경우
#         if c_flag:
#             current_time+=t
#             position=p_dic[position]
#
#         #도착한 곳에서 손님을 태우지 못한 경우
#         else :
#             opposite_customers = c_dic[p_dic[position]]
#             #양쪽 손님 중 현재 위치가 더 빨리 도착
#             if current_customers and opposite_customers and current_customers[0][0]<=opposite_customers[0][0]:
#                 current_time = current_customers[0][0]
#             #양쪽 손님 중 반대 위치가 더 빨리 도착
#             elif current_customers and opposite_customers and current_customers[0][0]>opposite_customers[0][0]:
#                 current_time = opposite_customers[0][0]+t
#                 position = p_dic[position]
#             #현재 위치에만 손님 남은 경우
#             elif current_customers and not opposite_customers:
#                 current_time = current_customers[0][0]
#             #반대 위치만 손님 남은 경우
#             elif not current_customers and opposite_customers:
#                 current_time = opposite_customers[0][0]+t
#                 position = p_dic[position]
#     return answer

def my(M:int, t:int, N:int, customers:List[int])->List[int]:
    current_time = 0
    left_customers = collections.deque()
    right_customers = collections.deque()
    answer =[-1]*N
    for idx,customer in enumerate(customers):
        if customer[1]=="left":
            left_customers.append([int(customer[0]),idx])
        else :
            right_customers.append([int(customer[0]),idx])

    p_dic = {"left":"right","right":"left"}
    c_dic = {"left":left_customers,"right":right_customers}
    position = "left"

    while len(left_customers)>0 or len(right_customers)>0:
        current_customers = c_dic[position]
        c_cnt = 0
        c_flag = False
        #도착한 곳에서 손님을 태우기
        while current_customers and int(current_customers[0][0])<=current_time\
            and c_cnt<M:
            pop_customer= current_customers.popleft()
            answer[pop_customer[1]] =current_time+t
            c_flag=True
            c_cnt+=1

        #손님을 태울 경우
        if c_flag:
            current_time+=t
            position=p_dic[position]

        #도착한 곳에서 손님을 태우지 못한 경우
        else:
            opposite_customers = c_dic[p_dic[position]]
            #양쪽 손님 중 현재 위치가 더 빨리 도착
            if current_customers and opposite_customers and current_customers[0][0]<=opposite_customers[0][0]:
                current_time = max(current_time,current_customers[0][0])
            #양쪽 손님 중 반대 위치가 더 빨리 도착
            elif current_customers and opposite_customers and current_customers[0][0]>opposite_customers[0][0]:
                current_time = max(current_time,opposite_customers[0][0])+t
                position = p_dic[position]
            #현재 위치에만 손님 남은 경우
            elif current_customers and not opposite_customers:
                current_time = max(current_time,current_customers[0][0])
            #반대 위치만 손님 남은 경우
            elif not current_customers and opposite_customers:
                current_time = max(current_time,opposite_customers[0][0])+t
                position = p_dic[position]
    return answer

# def my(M:int, t:int, N:int, customers:List[int])->List[int]:
#     left_queue = collections.deque()
#     right_queue = collections.deque()
#     answer = [0]*N
#     for idx,customer in enumerate(customers):
#         if customer[1] =="left":
#             left_queue.append([int(customer[0]),idx])
#         else :
#             right_queue.append([int(customer[0]),idx])
#     position = "left"
#     current_time = 0
#
#     while len(left_queue) + len(right_queue)>0:
#         flag = False
#         if left_queue and left_queue[0][0]<=current_time:
#             flag=True
#             if position =="left":
#                 position = "right"
#                 cnt=0
#                 while left_queue and left_queue[0][0]<=current_time and cnt<M:
#                     c = left_queue.popleft()
#                     answer[c[1]]=current_time+t
#                     cnt+=1
#                 current_time+=t
#             else :
#                 current_time+=t
#                 cnt =0
#                 while left_queue and left_queue[0][0]<=current_time and cnt<M:
#                     c = left_queue.popleft()
#                     answer[c[1]]=current_time+t
#                     cnt+=1
#                 current_time+=t
#         if right_queue and right_queue[0][0] <=current_time:
#             flag = True
#             if position =="right":
#                 position="left"
#                 cnt=0
#                 while right_queue and right_queue[0][0]<=current_time and cnt<M:
#                     c = right_queue.popleft()
#                     answer[c[1]]=current_time+t
#                     cnt+=1
#                 current_time+=t
#             else :
#                 current_time+=t
#                 cnt = 0
#                 while right_queue and right_queue[0][0] <= current_time and cnt < M:
#                     c = right_queue.popleft()
#                     answer[c[1]] = current_time + t
#                     cnt += 1
#                 current_time += t
#         if not flag:
#             current_time+=1
#     return answer

TC = int(input())
for test_case in range(1, TC + 1):
    M,t,N = map(int,sys.stdin.readline().rstrip().split())
    input_custom = []
    for i in range(N):
        input_custom.append(list(sys.stdin.readline().rstrip().split()))
    answer = my(M,t,N,input_custom)
    for i in answer:
        print(i)
