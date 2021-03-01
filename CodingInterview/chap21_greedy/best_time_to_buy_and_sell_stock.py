import sys
sys.stdin = open('input/best_time_to_buy_and_sell_stock')
from typing import List

def my(stocks :List[int])->int:
    result = 0
    for i in range(len(stocks)-1):
        if stocks[i]<stocks[i+1]:
            result+=stocks[i+1]-stocks[i]
    return result

def max_profit(prices:List[int])->int:
    result = 0
    for i in range(len(prices)-1):
        if prices[i+1]>prices[i]:
            result+=prices[i+1]-prices[i]
    return result

def pythonic(prices:List[int])->int:
    return sum(max(prices[i+1],prices[i]) for i in range(len(prices)-1))


stocks = list(map(int,input().split()))
my(stocks)