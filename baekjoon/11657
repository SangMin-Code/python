import sys

N,M=map(int,sys.stdin.readline().split())#도시개수 버스 노선개수

G=[]

for _ in range(M):

    G.append(list(map(int,sys.stdin.readline().split())))#출발 도착 거리



INF=sys.maxsize

result=[INF for _ in range(N+1)]

result[1]=0#자신으로 가는길만 초기화

check=0#음의 싸이클 체크

for i in range(N):#노드 갯수만큼 반복

    for j in range(M):#모든간선을 확인하며 거리갱신

        s=G[j][0]#출발

        e=G[j][1]#도착

        d=G[j][2]#거리

        if result[s]!=INF and result[e]>result[s]+d:#이전거리보다 작아서 갱신해야 한다면

            result[e]=result[s]+d

            if i==N-1:#N번돌았을때 갱신된다면

                check=1#음의 사이클이 있다



if check:

    print(-1)

else:

    for i in range(2,N+1):

        if result[i]==INF:

            print(-1)

        else:

            print(result[i])
