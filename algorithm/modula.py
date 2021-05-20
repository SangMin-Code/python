'''
모듈러 연산

1. (a mod n + b mod n) mod n = (a+b) mod n
2. (a mod n - b mod n) mod n = (a-b) mod n
3. (a mod n * b mod n) mod n = (a*b) mod n

모듈러 연산을 이용한 지수 구하기

11**7 mod 13 을 구할때
11**2 = 121 = 4 (mod13)
11**4 = (11**2)**2 = 4**2 = 3 (mod13)
11**7 = (11*4*3) = 132 = 2 (mod13)

출처 :https://developer-mac.tistory.com/84
'''