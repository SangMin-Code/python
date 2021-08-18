# Q4.py.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q4')


def my(genres:List[str],plays:List[str])->List[int]:
    genre_order = collections.defaultdict(int)
    song_order = collections.defaultdict(list)
    answer = []
    for i in range(len(genres)):
        genre,play = genres[i],int(plays[i])
        genre_order[genre]+=play
        song_order[genre].append([i,play])
        song_order[genre]=sorted(song_order[genre],key=lambda x:x[1],reverse=True)
    for genre,val in collections.Counter(genre_order).most_common():
        l = 2
        if len(song_order[genre])<2:
            l=1
        for i in range(l):
            answer.append(song_order[genre][i][0])
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    genres = list(input().split())
    plays = list(input().split())
    answer = my(genres,plays)
    print(answer)
