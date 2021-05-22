'''
제곱 구하기

 지수가 큰 제곱수를 구할때 사용.
 지수가 n으로 주어질 때, 제곱으로 나누는 방식을 이용함
 -> 지수를 2로 나눈 나머지가 1일 때 해당 단계의 수를 곱하는 것을 반복


  result,n,number = 1,11,3

  while n:
    if n%2:
        result *= number
    number *= number
    n//=2

'''