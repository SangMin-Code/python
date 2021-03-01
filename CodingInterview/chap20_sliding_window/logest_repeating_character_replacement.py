import sys
sys.stdin = open('input/logest_repeating_character_replacement')
import collections


def my(k:int, s:str)->int:
    #문자열이 항상 연속되있는 경우에만 성립 ex)AAABBB 가능, AABAB 불가
    queue = collections.deque(s[0])
    val = float('-inf')
    for i,char in enumerate(s[1:]):
        if char == queue[-1]:
            queue.append(char)
            if len(queue)==len(s):
                return len(queue)
        else :
            if len(queue)>val:
                val = len(queue)
            queue.clear()
            queue.append(char)
    return min(val+k,len(s))

def character_replacement(s:str, k:int)->int:
    left = right = 0
    counts = collections.Counter()
    for right in range(1,len(s)+1):
        counts[s[right-1]]+=1
        max_char_n = counts.most_common(1)[0][1]
        if right-left - max_char_n>k:
            counts[s[left]]-=1
            left+=1
    return right-left

def practice(s:str, k:int)->int:
    left= right = 0
    counts = collections.Counter()
    for right in range(1,len(s)+1):
        counts[s[right-1]]+=1
        max_char_n = counts.most_common(1)[0][1]
        if right -left -max_char_n >k:  #최대 길이가 되기 위해서는 right가 최대, left가 최소여야 한다.
            counts[s[left]]-=1          #right-left-max_char_n =k 이후 right, left가 같이 증가
            left+=1
    return right-left


k = int(input())
s = input()
#answer = my(k,s)
answer = practice(s,k)
print(answer)