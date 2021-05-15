# plus_minus.py
import sys
from typing import List

sys.stdin = open('input/plus_minus')


def my(absolutes, signs):
    answer =0
    for i in range(len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer


answer = my([4,7,12],[True,False,True])
print(answer)
