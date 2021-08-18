def grader(name:str,score:str):
    try:
        score = int(score)
        if score<0:
            raise ValueError
    except ValueError:
        print("점수는 숫자를 입력해주세요.")
        return

    if score<0 or score>100:
        print(f'{score}는 유효하지 않은 점수입니다.')
        return

    grade = ''
    if score>=95:
        grade='A+'
    elif score>=90:
        grade='A'
    elif score>=85:
        grade='B+'
    elif score>=80:
        grade='B'
    elif score>=75:
        grade='C+'
    elif score>=70:
        grade='C'
    elif score>=65:
        grade='D+'
    elif score>=60:
        grade='D'
    else:
        grade='F'
    print(f'학생이름 : {name}')
    print(f'점수 : {score}점')
    print(f'학점 : {grade}')


name = input("이름을 입력해주새요 : ")
score = input("점수를 입력해주세요 : ")
grader(name,score)












