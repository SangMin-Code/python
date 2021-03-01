
def hammingweight(n:int)->int:
    return bin(n).count('1')

def using_bit(n:int)->int:
    count=0
    while n:
        n &= n-1
        count+=1
    return count

#TODO 비트연산