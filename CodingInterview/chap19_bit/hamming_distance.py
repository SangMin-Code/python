import sys
sys.stdin = open('input/hamming_distance')

def my(x:int, y:int)->int:
    return bin(x^y).count('1')




x = int(input())
y = int(input())
answer = my(x,y)
print(answer)