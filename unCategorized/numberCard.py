#numberCard

a=12345111
list = [0]*9

while(a>0):
    list[a%10]+=1
    a=int(a/10)
max = max(list)
print(list)

b = list.index(max,-1,0)

print(b)

