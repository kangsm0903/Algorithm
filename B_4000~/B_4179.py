# 4179

from collections import deque

n,m=map(int,input().split())

graph=[list(map(str,input())) for _ in range(n)]
# ####
# #JF#
# #..#
# #..#

queue_jihun=deque([])
queue_fire=deque([])

graph_j=[[0]*m for _ in range(n)] # 지훈이 위치 그래프
graph_f=[[0]*m for _ in range(n)] # 화재 위치 그래프

dx=[-1,1,0,0] # 상 하
dy=[0,0,-1,1] # 좌 우

for i in range(n):
    for j in range(m):
        if graph[i][j]=='J':
            graph_j[i][j]=1
            queue_jihun.append((i,j))
        elif graph[i][j]=='F':
            graph_f[i][j]=1
            queue_fire.append((i,j))

def bfs():
    # 화재 먼저
    while queue_fire:
        x,y=queue_fire.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 범위 내에 존재하고, 전체 graph에서 (nx,ny)가 '#'이 아니라면
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]!='#' and graph_f[nx][ny]==0:
                    graph_f[nx][ny]=graph_f[x][y]+1
                    queue_fire.append((nx,ny))
    
    while queue_jihun:
        x,y=queue_jihun.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]!='#' and graph_j[nx][ny]==0:
                    
                    if graph_f[nx][ny]>graph_j[x][y]+1 or graph_f[nx][ny]==0:
                        graph_j[nx][ny]=graph_j[x][y]+1
                        queue_jihun.append((nx,ny))
            else:
                return graph_j[x][y]
    return 'IMPOSSIBLE'

print(bfs())