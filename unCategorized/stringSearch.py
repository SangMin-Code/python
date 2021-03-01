#stringSearch.py

'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''


fstr = "ZYJZXZTIBSDG"
tstr = "TTXGZYJZXZTIBSDGWQLW"

list = []

for i in range(len(tstr)-len(fstr)+1):
    list.append(tstr[i:len(fstr)+i])
print(list)
if fstr in list : print(1)
else : print(0)