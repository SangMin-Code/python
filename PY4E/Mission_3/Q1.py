
def gugudan(num:int):
    print(f'{number}단')
    for i in range(1,10):
        if i%2 and num*i<=50:
            print(f'{num} x {i} = {num*i}')

while True:
    number = input('몇 단? :').strip()

    if not number.isdecimal() or not (0<int(number)<10):
        print('1 이상 9 이하의 숫자가 아닙니다.')
    else:
        number = int(number)
        break

gugudan(number)