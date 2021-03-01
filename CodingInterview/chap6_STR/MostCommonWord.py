#MostCommonWord.py
import sys
import re
from typing import List
from collections import defaultdict
import collections
sys.stdin = open('input/MostCommonWord','r')

def my(s:str, banned:str)->str:
    s=s.lower()
    s=re.sub('[^a-z0-9 ]','',s)
    tempList = list(s.split())
    dic = defaultdict(int)
    for i in tempList:
        dic[i]+=1
    dic[banned]=0
    return (max(dic,key=dic.get))  #max(dic) key 중 최댓값, key=dic.get을 사용하면 value가 최대인 key값을 얻음

def most_common_word(paragraph:str, banned:List[str])->str:
    words = [word for word in re.sub(r'[^\w]',' ',paragraph)
             .lower().split()
                 if word not in banned]

    #counts = defaultdict(int)
    #for word in words:
    #    counts[word]+=1
    #return max(counts,key=counts.get)
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


s=input()
banned = input()
#print(my(s,banned))
print(most_common_word(s,banned))