def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    seaList=[]

    while queue:
        x,y=queue.popleft()
        visited[x][y]=1
        sea=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                # 주변이 바다라면 sea+=1
                if graph[nx][ny]==0 and visited[nx][ny]==0:
                    sea+=1
                # 주변이 빙하라면 queue에 추가
                elif graph[nx][ny]>0 and visited[nx][ny]==0:
                    queue.append((nx,ny))
                    visited[nx][ny]=1
        if sea>0:
            seaList.append((x,y,sea))
    
    for x, y, sea in seaList:
        graph[x][y]=max(0,graph[x][y]-sea)
                
    return 1

from collections import deque

N,M=list(map(int,input().split()))

graph=[list(map(int,input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

ice=[]

# 빙하의 위치 할당
for i in range(N):
    for j in range(M):
        if graph[i][j]>0:
            ice.append((i,j))

year=0

while ice:
    group=0
    visited=[[0]*M for _ in range(N)]
    delList=[]
    
    for i,j in ice:
        # 빙하가 존재하는 경우
        if graph[i][j]>0 and visited[i][j]==0:
            group+=bfs(i,j)
        # 빙하가 다 녹은 경우
        if graph[i][j]==0 and visited[i][j]==1:
            delList.append((i,j))

    if group>1:
        print(year)
        break

    ice=list(set(ice)-set(delList))
    year+=1

if group<2:
    print(0)

# --------------------------------------------------------------------------------
# 빙하 지역 카운트를 dfs로 설계해서 dfs, bfs 둘 다 구현하다보니 시간,메모리 초과 발생

import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(x,y): # 몇개로 분리되었는지 카운트
    if x<0 or y<0 or x>=N or y>=M:
        return False

    if graph[x][y]>0 and visited[x][y]==False:
        visited[x][y]=True
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

def bfs():  # 1년마다 줄어드는 빙하
    while ice_location:
        x,y=ice_location.popleft()

        visited[x][y]=True # 방문 체크

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]<=0 and visited[nx][ny]==False:
                    graph[x][y]-=1
                    # if graph[x][y]<0:
                    #     graph[x][y]=0
input=sys.stdin.readline

N,M=map(int,input().split())

graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(N):
    graph.append(list(map(int,input().split())))

result=0
visited=[[False]*M for _ in range(N)]
for i in range(N):      # 현재 분리된 빙하의 갯수 확인
    for j in range(M):
        if dfs(i,j)==True:
            result+=1

loop_cnt=0
while result<2:
    loop_cnt+=1

    ice_location=deque()    # 빙하 위치를 담을 큐

    for i in range(N):      # 빙하 위치 삽입
        for j in range(M):
            if graph[i][j]>0:
                ice_location.append([i,j])
    visited=[[False]*M for _ in range(N)]
    bfs()   # 녹은 빙하의 상태 갱신

    result=0
    visited=[[False]*M for _ in range(N)]
    for i in range(N):      # 분리된 빙하의 갯수 확인
        for j in range(M):
            if dfs(i,j)==True:
                result+=1

    target=0
    for i in graph:
        target=max(target,max(i))
    if target==0:
        loop_cnt=0
        break

print(loop_cnt)