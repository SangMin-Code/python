def add(a,b):
    return a+b
def sub(a,b):
    return a-b
if __name__=="__main__":
    print(add(1,4))
    print(sub(4,2))

list =[]
sum = 0
for i in range(1000):
    if i %3 ==0 or i%5==0 :
        sum+=i
print(sum)


def getTotalPage(m,n):
    result = m//n
    if m%n!=0:
        result+=1
    return result

