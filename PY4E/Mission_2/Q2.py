def calculator(monthly_payment):
    try:
        monthly_payment = int(monthly_payment)
        if monthly_payment<0:
            raise ValueError
    except ValueError:
        print('숫자로만 입력해주세요.')
        return
    pre_tax,after_tax = 12*monthly_payment,0

    if pre_tax<=1200:
        after_tax = int(pre_tax*0.94)
    elif pre_tax<=4500:
        after_tax = int(pre_tax*0.85)
    elif pre_tax<=8800:
        after_tax = int(pre_tax*0.76)
    elif pre_tax<=15000:
        after_tax = int(pre_tax*0.65)
    elif pre_tax<=30000:
        after_tax = int(pre_tax*0.62)
    elif pre_tax<=30000:
        after_tax = int(pre_tax*0.60)
    else:
        after_tax = int(pre_tax*0.58)
    print(f'세전 연봉: {pre_tax}만원')
    print(f'세전 연봉: {after_tax}만원')



monthly_payment = input("월급을 입력해주세요 (만원) : ")
calculator(monthly_payment)
