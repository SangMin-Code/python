import os.path

def count_word() :
    while True:
        fileName = input("파일명을 입력해주새요 : ")
        if not os.path.isfile(f'storage/{fileName}.txt'):
            break
        print('이미 존재하는 파일입니다.')

    f= open(f'storage/{fileName}.txt', 'w',encoding='utf8')

    print('텍스트를 입력해 주세요 : ')
    lines =[]

    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    word = input("찾으려는 단어를 입력해주세요 :")
    cnt = 0
    for line in lines:
        cnt += line.count(word)
        f.write(line+'\n')
    print(f'{word}는 {cnt}개 있습니다.')
    f.close()


count_word()