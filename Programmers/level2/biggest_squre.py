#https://programmers.co.kr/learn/courses/30/lessons/12905
#효율성 문제 timeout
#https://soobarkbar.tistory.com/164
#https://velog.io/@diddnjs02/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0
import sys
sys.stdin = open('input/biggest_squre')
from typing import List

def my(squre:List[List[int]])->int:
    def find_squre(row, col):
        available = min(len(squre)-row, len(squre[row])-col)
        val = 1
        for i in range(available,1,-1):
            flag = True
            for j in range(i):
                for k in range(i):
                    if squre[row+j][col+k]==0:
                        flag= False
                        break
                if not flag:
                    break
            if flag :
                val = i
                break
        return val

    answer =0

    if len(squre)==1:
        return 1

    for i in range(len(squre)):
        for j in range(len(squre[i])):
            answer = max(find_squre(i,j),answer)
            if answer >= len(squre[i]) - j:
                break
        if answer >= len(squre) - i:
            break
    return answer**2

def my2(squre:List[List[int]])->int:
    def find_squre(row,col):
        available = min(len(squre)-row,len(squre[row])-col)
        val =1
        for i in range(available,1,-1):
            flag = True
            for j in range(row,row+i,1):
                if 0 in squre[j][col:col+i]:
                    flag = False
                    break
                if not flag:
                    break
            if flag :
                val = i
                break
        return val
    answer =0
    for i in range(len(squre)):
        for j in range(len(squre[i])):
            answer = max(find_squre(i,j),answer)
    return answer

def my3(board:List[List[int]])->int:
    row = len(board)
    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
    answer = []
    for i in range(row):
        answer.append(max(board[i]))
    return max(answer) ** 2

def practice(board:List[List[int]])->int:
    row = len(board)
    col = len(board[0])

    for i in range(1,row):
        for j in range(1,col):
            if board[i][j]==1:
                board[i][j]=min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
    answer = []
    for i in range(row):
        answer.append(max(board[i]))
    return max(answer)**2



TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    squre = []
    for _ in range(n):
        squre.append(list(map(int,input().split())))
    answer = my3(squre)
    print(answer)