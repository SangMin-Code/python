import datetime


def after_100():
    year,month,date = 0,0,0
    weekday = '월화수목금토일'
    DAYS = 100
    date = datetime.datetime.now()
    while True:
        try:
            date = input('몇년 몇월 며칠인지 입력해주세요. ex) 2021 8 12 :')
            year,month,date = map(int,date.split())
            date = datetime.datetime(year,month,date)
            break
        except ValueError:
            print('유효한 날짜를 입력해주세요.')

    plus_days = datetime.timedelta(days=DAYS)
    after_date = date+plus_days



    print(f'{date.year}년 {date.month}월 {date.day}일 {weekday[date.weekday()]}요일로부터 \
    {DAYS}일 후는 {after_date.year}년 {after_date.month}월 {after_date.day}일 {weekday[after_date.weekday()]}요일')


after_100()
