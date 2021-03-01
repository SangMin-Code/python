#stringSearch2


'''
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
'''

n = 10
m = 10
str = ''
str2= ''
list = ['GOFFAKWFSM','OYECRSLDLQ','UJAJQVSYYC','JAEZNNZEAJ','WJAKCGSGCF'
        ,'QKUDGATDQL','OKGPFPYRKQ','TDCXBMQTIO','UNADRPNETZ','ZATWDEKDQF']

for i in range(n):
    temp = ''
    for j in range(n):
        temp += list[j][i:i+1]
    list.append(temp)
print(list)
result = ''

for i in range(2*n):
    for j in range(n-m+1):
        str =list[i][j:j+m]
        flag = True
        for k in range(0,m//2):
            if str[k] != str[-k-1]:
                flag = False
                break
        if flag : result = str
print(result)

