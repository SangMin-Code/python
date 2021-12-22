import sys

sys.stdin = open('Programmers/level2/input/rotate_bracket.txt')


def solution(brackets: str) -> int:
    result = 0
    if brackets.count('(') != brackets.count(')') or\
            brackets.count('[') != brackets.count(']') or\
            brackets.count('{') != brackets.count('}'):
        return 0

    for i in range(len(brackets)):
        # print(len(brackets[i:]))
        rotate_brackets = brackets[i:]+brackets[:i]
        result += is_correct(rotate_brackets)
    return result


def is_correct(s: str) -> int:
    if s[0] == '}' or s[0] == ')' or s[0] == ']':
        return 0

    bracket_dic = {")": "(", "]": "[", "}": "{"}
    stack = [s[0]]
    for i in range(1, len(s)):
        if s[i] == '}' or s[i] == ')' or s[i] == ']':
            if not stack:
                return 0
            if bracket_dic[s[i]] != stack[-1]:
                return 0
            else:
                stack.pop()
        else:
            stack.append(s[i])
    return 1


TC = int(input())
for i in range(TC):
    brackets = input()
    result = solution(brackets)
    print(result)
