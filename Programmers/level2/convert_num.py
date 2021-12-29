import sys
sys.stdin = open('Programmers/level2/input/convert_num.txt')

def my(s:str)->str:
    answer =""
    dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4",
           "five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

    num = ""
    for i in s:
        if not i.isdigit():
            num+=i
            if num in dic:
                answer+=dic[num]
                num=""
        else :
            answer+=i
    return answer

TC = int(input())
for test_case in range(1,TC+1):
    s=input()
    answer = my(s)
    print(answer)