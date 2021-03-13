#search_ranking.py
import sys
import bisect
sys.stdin=open('input/search_ranking')
from typing import List
import collections

def my(infp:List[str], query:List[str])->List[int]:
    result =[]
    for_serach = []
    for i in info:
        temp = i.split()
        for_serach.append([' '.join(temp[:-1]),int(temp[-1])])
    for_serach.sort(key=lambda x:x[1])

    for i in query:
        conditions =[]
        score =0
        cnt =0
        for condition in i.split():
            if not condition.isdigit() and condition !='and' and condition != '-' :
                conditions.append(condition)
            elif condition.isdigit():
                score = int(condition)
        idx = bisect.bisect_left([x[1] for x in for_serach], score)
        temp = for_serach[idx:]
        for man in temp:
            flag = True
            for condition in conditions:
                if condition not in man[0]:
                    flag = False
                    break
            if flag:
                cnt+=1
        result.append(cnt)
    print(result)


def my2(info:List[str], query:List[str])->List[int]:
    total_group = collections.defaultdict(list)
    result = []
    def make_group(n):
        if n ==4:
            if not total_group[''.join(group)]:
                total_group[''.join(group)] = [int(temp[-1])]
            else :
                for_sort =total_group[''.join(group)].append(int(temp[-1]))
        elif n<4:
            #print(group)
            candidate = ['-',temp[n]]
            for i in candidate:
                group.append(i)
                make_group(n+1)
                group.pop()

    for i in info:
        temp = list(i.split())
        group =[]
        make_group(0)

    for i in query:
        i = i.replace('and','')
        temp = i.split()
        score = temp[-1]
        sorted_list = total_group[''.join(temp[:-1])]
        if sorted_list:
            sorted_list.sort()
            idx = bisect.bisect_left(sorted_list,int(score))
            print(sorted_list,idx,score)
            result.append(len(sorted_list)-idx)
    return result

# 16가지의 경우의 수를 만들어주는 함수
def make_cases():
    global changes, tmp
    if len(tmp) == 4:
        t = []
        for index in tmp: t.append(index)
        changes.append(t)
        return

    for i in (False, True):
        tmp.append(i)
        make_cases()
        tmp.pop()


# True를 가리키는 인덱스에 해당하는 속성 값을 '-'으로 바꿔준다.
def replace(change, data):
    for i in range(4):
        if change[i]: data[i] = '-'

    return data


def copy(data):
    _data = []
    for item in data: _data.append(item)

    return _data


def search(scores, num):
    size = len(scores)
    return size - bisect.bisect_left(scores, num, lo=0, hi=size)


def solution(info, query):
    global changes
    answer = []
    info_dict = {}
    make_cases()

    # query를 위한 info 전처리
    for data in info:
        data = data.split()
        score = int(data[-1])
        data = data[:4]

        for change in changes:
            _data = copy(data)
            _data = replace(change, _data)
            _data = ''.join(_data)

            if _data not in info_dict.keys():
                info_dict[_data] = [score]
            else:
                info_dict[_data].append(score)

    # info_dict[key] 정렬
    for key in info_dict.keys(): info_dict[key].sort()

    for q in query:
        q = q.split()
        score = int(q[-1])
        _q = ''

        # query 문자열 처리
        for item in q[:len(q) - 1]:
            if item != 'and': _q += item

        # 문의 조건을 만족하는 지원서들의 수 찾기
        if _q not in info_dict.keys():
            answer.append(0)
        else:
            cnt = search(info_dict[_q], score)
            answer.append(cnt)

    return answer


TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    info = []
    query =[]
    for _ in range(n):
        info.append(input())
    n = int(input())
    for _ in range(n):
        query.append(input())
    answer = my2(info,query)
    print(answer)