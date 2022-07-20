from collections import deque

m,n=map(int,input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
# graph=[list(map(int,input().split())) for i in range(n)]

queue=deque([])

dx=[-1,1,0,0] # 상 하
dy=[0,0,-1,1] # 좌 우

result=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j))

def bfs():
    while queue:
        # queue에 들어있는 익은 토마토의 좌표를 가져옴
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==1 or graph[nx][ny]==-1:
                continue

            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

            # if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            #     graph[nx][ny]=graph[x][y]+1
            #     queue.append((nx,ny))

bfs()

for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    result=max(result,max(i))
# 시작을 1로 표현했으니 1을 빼줌
print(result-1)