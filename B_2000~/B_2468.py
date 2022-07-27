# 높이는 1이상 100이하 정수
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    
    if graph[x][y]>T and visited[x][y]==False:
        visited[x][y]=True # 방문처리
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

N=int(input())

graph=[]

for i in range(N):
    graph.append(list(map(int,input().split())))

result=[]

target=0

for i in graph:
    target=max(target,max(i))

for T in range(target):
    visited=[[False]*N for _ in range(N)]

    cnt=0
    for i in range(N):
        for j in range(N):
            if dfs(i,j)==True:
                cnt+=1

    result.append(cnt)

print(max(result)) 

# ----------------------------------------------------------------------------------

import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,target):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny]>T and visited[nx][ny]==False:
                visited[nx][ny]=True
                dfs(nx,ny,target)

N=int(input())

graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    graph.append(list(map(int,input().split())))

result=[]

target=0

for i in graph:
    target=max(target,max(i))

for T in range(target):
    visited=[[False]*N for _ in range(N)]
    cnt=0

    for i in range(N):
        for j in range(N):
            if graph[i][j]>T and visited[i][j]==False:
                cnt+=1
                visited[i][j]=True
                dfs(i,j,T)

    result.append(cnt)

print(max(result)) 