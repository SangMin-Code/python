def find_prime(a,b):
    cnt =0
    for i in range(a+1,b):
        if is_prime(i):
            cnt+=1
    print(f'소수 개수 : {cnt}')

def is_prime(num):
    for i in range(2,int(num**0.5)+1,1):
        if not num%i:
            return False
    return True

while True:
    n = input("첫번째 수 입력 n:")
    m = input("두번째 수 입력 m:")
    if not n.isdecimal() or not m.isdecimal() or int(n)<0 or int(m)<0:
        print("1이상의 자연수만 입력해주세요.")
    else:
        n,m = int(n),int(m)
        break


find_prime(min(n,m),max(n,m))