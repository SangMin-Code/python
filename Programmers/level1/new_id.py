import sys
sys.stdin = open('Programmers/level1/input/new_id.text')


def solution(id: str):
    # 모두 소문자
    id = id.lower()
    # 알파벳 소문자, 숫자, - , _ , . , 제외 제거
    id = ''.join(i for i in id if i.isdecimal() or i.isalpha() or i in [
                 '-', '_', '.'])
    # 연속된 . 제거
    stack = [id[0]]
    for i in range(1, len(id)):
        if stack[-1] == id[i] == '.':
            stack.pop()
        stack.append(id[i])
    id = ''.join(stack)
    # id 맨 앞 뒤 . 제거
    if id.startswith('.'):
        id = id[1:]
    if id.endswith('.'):
        id = id[:-1]
    # id가 빈 문자열이면 a를 대입
    if id == '':
        id = 'a'
    # 길이가 16자 이상이면 15자로 줄임, 맨 뒤  . 제거
    if len(id) > 15:
        id = id[:15]
        if id.endswith('.'):
            id = id[:-1]
    # 길이가 2자 이하면 마지막 문자를 길이가 3이될때까지 붙임
    if len(id) < 3:
        while len(id) < 3:
            id = id+id[-1]

    return id


TC = int(input())
for i in range(TC):
    new_id = input()
    print(solution(new_id))
