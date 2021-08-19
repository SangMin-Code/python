from typing import List


def manageMember(names:List[str],records:List[List[int]]):
    dic = {}
    for idx,name in enumerate(names):
        dic[name] = sum(records[idx])/len(records[idx])

    bonus= []
    interview =[]
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    for i in range(0,2):
        if dic[i][1] > 5:
            bonus.append(dic[i][0])
        if dic[-i-1][1] <= 3:
            interview.append(dic[-i-1][0])

    for i in bonus:
        print(f'보너스 대상자 {i}')
    print()
    for i in interview:
        print(f'면담 대상자 {i}')


member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

manageMember(member_names,member_records)