import sys
sys.stdin = open('input/differnet_ways_to_add_parentheses')
from typing import List

#TODO 괄호를 삽입하는 여러 가지 방법 - 분할정복
def diffWaysToCompute(input:str)->List[int]:
    def compute(left, right, op):
        results=[]
        for l in left:
            for r in right:
                results.append(eval(str(l)+op+str(r)))
        return results

    if input.isdigit():
        return [int(input)]

    results =[]
    for index, value in enumerate(input):
        if value in '-+*':
            left = diffWaysToCompute(input[:index])
            right = diffWaysToCompute(input[index+1:])

            results.extend(compute(left,right,value))
    return results


TC = int(input())
for test_case in range(1,TC+1):
    expression = input()
