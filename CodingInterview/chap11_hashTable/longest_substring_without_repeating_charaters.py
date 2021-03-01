#longest_substring_without_repeating_charaters

import sys
sys.stdin=open('input/longest_substring_without_repeating_charaters')
import collections

'''
abcabccbb
pwwkeww

'''
def my(s:str)->int:
    test = answer = ''
    max_length = 0
    start = end = 0
    seen = []
    for idx, str in enumerate(s) :
        if str not in seen :
            end = idx
            maxlength = max(max_length, end-start)
            answer = s[start:end+1]
            #print('answer',answer)
            seen.append(str)
            #print(start,end,answer,max+1)
        else :
            start,end = idx,idx+1
            test =s[start:end]
            #print('test',test)
    return max_length+1

def length_of_longest_string(s:str)->int:
    used ={}
    max_length = start = 0
    for index, char in enumerate(s):
        #이미 등장했던 문자라면 start 위치 갱신
        if char in used and start<=used[char]:
            start = used[char]+1
        else : #최대 부분 문자열 길이 갱신
            max_length = max(max_length, index-start+1)
        #현재 문자의 위치 삽입
        used[char]=index
    return max_length



TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    print(my(s))

