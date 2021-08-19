from typing import List

def duplicated(korea_list:List[str],chosun_list:List[str]):

    duplicated_set = set(korea_list) & set(chosun_list)

    for i in duplicated_set:
        print(f'조선과 고려에 모두 있는 왕 이름 : {i}')
    print(f'조선과 고려에 모두 있는 왕 이름은 총 {len(duplicated_set)} 개 입니다.')

#왕이름
korea_king = '태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕'
chosun_king = '태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종'

korea_list = korea_king.split(',')
chosun_list = chosun_king.split(',')

duplicated(korea_list,chosun_list)

