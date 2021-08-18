
def find_even(a,b):
    if a==b:
        print('a와 b 사이에 숫자가 존재하지 않습니다.')
        return
    for i in range(a+1,b):
        if not i%2:
            if i==(a+b)//2:
                print(f'{i} 중앙값')
            else:
                print(f'{i} 짝수')

while True:
    n = input("첫번째 수 입력 n:")
    m = input("두번째 수 입력 m:")
    if n.isdecimal() and m.isdecimal():
        n,m = int(n),int(m)
        break

find_even(min(n,m),max(n,m))
