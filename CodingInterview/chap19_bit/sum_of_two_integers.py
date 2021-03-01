import sys
sys.stdin = open('input/sum_of_two_integers')

#TODO 전가산기 구현 559p
def get_sum(a:int, b:int)->int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)

    result = []
    carry = 0
    sum = 0

    for i in range(32):
        A = int(a_bin[31-i])
        B = int(b_bin[31-i])

        Q1 = A&B
        Q2 = A^B
        Q3 = Q2 & carry
        sum = carry^Q2
        carry = Q1|Q3

        result.append(str(sum))
    if carry ==1:
        result.append('1')

    result = int(''.join(result[::-1]),2)&MASK
    if result>INT_MAX:
        result = ~(result^MASK)
    return result

def short(a:int, b:int)->int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    while b!=0:
        a,b = (a^b)&MASK, ((a&b)<<1)&MASK

    if a >INT_MAX:
        a = ~(a^MASK)
    return a

TC = int(input())
a,b = map(int,input().split())
