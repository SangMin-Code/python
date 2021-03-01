#stringSearch3

'''
XYPV
EOGGXYPVSY
'''

string_list = 'XYPVASDASDASD'
string = 'EOGGXYPVSY'
dic = {string : 0 for string in string_list}

list = ['A','B','C','D','E','F','G','H','I','J','K','L','M'',N','O','P','Q','R','S','T','U'
        ,'V','W','X','Y','Z',
        'a','b','c','d','e,','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'
        ,'v','w','x','y','z']
dic = {}
for i in string_list:
    if list.index(i)!=-1 :
        dic[list.index(i)]=0
for i in string :
    if list.index(i) in dic:
        print(i,list.index(i))
        dic[list.index(i)] +=1

#print(max(dic.values()))
print(dic)



