#best_album
#programmers.co.kr/learn/courses/30/lessons/42579#
import sys
sys.stdin=open('input/best_album')
from typing import List
import collections

def my(genres:List[str], plays:List[int])->List[int]:
    answer = []
    dic = collections.defaultdict(list)  #장르별 곡과 재생횟수
    genre_sum = collections.defaultdict(int)  #장르별 재생횟수

    for i in range(len(genres)):
        dic[genres[i]].append([i,plays[i]])
        dic[genres[i]].sort(key=lambda x: [x[1],-x[0]])  #재생횟수가 같을 경우 고유번호가 낮은 곡 우선
        genre_sum[genres[i]]+=plays[i]
    genre_sum = sorted(genre_sum.items(),key=lambda x:x[1],reverse=True)

    for genre,val in genre_sum:
        for _ in range(2):
            if not dic[genre]:
                continue
            answer.append(dic[genre].pop()[0])
    return answer


TC = int(input())
for test_case in range(1,TC+1):
    genres = list(input().split())
    plays = list(map(int,input().split()))
    answer =my(genres,plays)
    print(answer)