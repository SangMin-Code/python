
def make_comma(num:str):
    #4자리 이상일 경우 찍음
    if len(num)<4:
        print(f'{num}')
    else:
        #결과값
        result = ''
        #뒤에서 부터 세야 하므로 문자열 뒤집기
        num = num[::-1]
        #뒤집은 문자열을 뒤에서부터 읽으며 3자리째에 콤마 추가하기


        for i,s in enumerate(num):
            result+=s
            if not (i+1)%3:
                result+=','
        print(result[::-1])

while True:
    num = input('숫자를 입력해주세요(,제외) : ')
    if num.isdecimal():
        make_comma(num)
        break
    else:
        print('숫자를 다시 입력해주세요.')


