#letter-combination-of-a-phone-number
from typing import List


def my(nums:List[str])->List[str]:
    result = []
    def find(i,s):
        for letter in dic[nums[i]]:
            if i==len(nums)-1:
                result.append(s+letter)
            else :
                find(i+1,s+letter)
    find(0,'')
    return result

def letterCombination(digits:str)->List[str]:
    def dfs(index,path):
        if len(path)==len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i+1,path+j)
    if not digits:
        return []
    result = []
    dfs(0,'')
    return result




dic = {
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
}
print(my(['2','3','4']))
