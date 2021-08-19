from typing import List


def  organaize(info:str):
    id,age,phone,gender,address,count=[],[],[],[],[],[]
    coupon = []

    info_list = info.split(',')

    for idx, info in enumerate(info_list):
        if idx%6==0:
            id.append(info)
        elif idx %6==1:
            age.append(info)
        elif idx%6==2:
            if info=='x':
                phone.append('000-0000-0000')
            else:
                phone.append(info)
        elif idx%6==3:
            gender.append(info)
        elif idx%6==4:
            address.append(info)
        elif idx%6==5:
            count.append(int(info))
    for idx in range(len(count)):
        if count[idx]>=8 and phone[idx]!='000-0000-0000':
            coupon.append([id[idx],age[idx],phone[idx],gender[idx],address[idx],count[idx]])

    print(f'아이디{id}, 나이{age},전화번호{phone},성별{gender},지역{address},구매횟수{count}')
    for i in coupon:
        print(f'아이디 {i[0]}, 나이 {i[1]},전화번호 {i[2]},성별 {i[3]},지역 {i[4]},구매횟수 {i[5]}')

info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
organaize(info)