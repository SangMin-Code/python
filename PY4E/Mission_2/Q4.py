def bus_fare(age,type):
    try:
        age = int(age)
        if age<=0:
            raise ValueError
    except ValueError:
        print("나이는 0보다 큰 숫자로 입력해주세요.")
        return

    if type!='카드' and type!='현금':
        print('현금/카드 중 선택해주세요.')
        return

    fare = 0

    if age<8:
        pass
    elif age<14:
        fare = 450
    elif age<20:
        if type=='카드':
            fare = 720
        else:
            fare = 1000
    elif age<75:
        if type=='카드':
            fare = 1200
        else:
            fare = 1300

    print(f'나이 : {age}')
    print(f'지불유형 : {type}')
    print(f'버스요금 : {fare}원')


age = input("나이를 입력해주세요 : ")
type = input("현금/카드를 선택해주세요. :")
bus_fare(age,type)