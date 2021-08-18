while True:
    check = input("생일이 지났으면 1, 아니면 0 을 입력하세요.")
    if check == '1' or '0':
        check = int(check)-1
        break
    else:
        print('0 또는 1을 입력해주세요.')

while True:
    age = input("한국 나이를 입력해주세요. (숫자)")
    if age.isdecimal():
        print(f'미국나이: {int(age)+check-1}')
        break
    else:
        print("숫자를 입력해주세요.")