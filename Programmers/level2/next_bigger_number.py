#https://programmers.co.kr/learn/courses/30/lessons/12911
import sys
sys.stdin = open('input/next_bigger_number')


def my(number:int)->int:
    binary = bin(number)[2:]
    count = binary.count('1')
    print(binary)
    if len(binary) == count:
        return int('10'+binary[1:],2)

    if len(binary)-1 ==count and number[-1]=='0':
        return int(binary[:-1]+1,2)
    if count ==1:
        return int(binary[:]+'0',2)

    idx = len(binary)-1
    for i,v in enumerate(binary[:-1]):
        if v=='0' and binary[i+1]=='1':
            idx = i
            break
        if v=='1' :
            count-=1
    print(binary[:idx] +'1'+ '0'* (len(binary[idx:]) - count) + '1' * (count-1))
    return int(binary[:idx] +'1'+ '0'* (len(binary[idx:]) - count) + '1' * (count-1),2)

def practice1(number:int)->int:
    #binary를 뒤쪽부터 흝어가면서 i,i+1 == 1,0인 idx 확인
    binary = bin(number)[2:]
    count = binary.count('1')
    binary = '0'+binary
    cnt =0
    for i in range( len(binary)-1, 0, -1):
        if binary[i] =='1':
            cnt+=1
        if binary[i]=='1' and binary[i-1]=='0':
            binary = binary[:i-1] +'10'+'0'*(len(binary)-i-cnt)  +'1'*(cnt-1)
            break
    return int(binary,2)



def my2(number:int)->int:
    binary = bin(number)[2:]
    count = binary.count('1')
    for i in range(number, 1000000):
        if bin(i)[2:].count('1')==count:
            return i

TC = int(input())
for test_case in range(1,TC+1):
    number= int(input())
    #answer = my(number)
    answer = practice1(number)
    print(answer)