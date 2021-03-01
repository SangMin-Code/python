#LongestPalindrome
import sys
sys.stdin = open('input/LongestPalindrome','r')

def my(s:str)->str:
    def exp(left:int,right:int)->str:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    if len(s)<2 or s==s[::-1]:
        return s
    result = ''
    for i in range(len(s)-1):
        result = max(result,
                     exp(i,i+1),
                     exp(i,i+2),
                     key = len)
    return result


def longesstPalindrome(s:str)-> str:
    #펠린드롬 판별 및 투 포인터 확장
    def expand(left:int, right:int)->str:
        while left>=0 and right<=len(s) and s[left]==s[right-1]:
            left-=1
            right+=1
        return s[left+1 : right]
    if len(s)<2 or s==s[::-1]:
        return s
    result = ''
    for i in range(len(s)-1):
        result = max(result,
                         expand(i,i+1),
                         expand(i,i+2),
                         key =len)
        return result

TC = int(input())
for test_case in range(1,TC+1):
    s=input()
    print(my(s))
    #print(longesstPalindrome(s))