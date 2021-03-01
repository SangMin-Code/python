#paper.py

cnt = [1,3]
def paper(n):
    if n >=2 and len(cnt)<=n:
        cnt.append(paper(n-1)+2*paper(n-2))
    return cnt[n]
paper(5)
print(cnt)