# 1. 섬을 숫자들로 구분
# 2. BFS로 돌다가 다른 섬을 만나면 기존의 거리와 최신 거리를 비교해서 짧은 거리로 갱신

from collections import deque

N=int(input())

graph=[list(map(int,input().split())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=200

def bfs1(a,b):
    global count

    queue=deque()
    queue.append((a,b))
    graph[a][b]=count
    visited[a][b]=1 # 방문 확인

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==1 and visited[nx][ny]==0:
                    graph[nx][ny]=count
                    visited[nx][ny]=1
                    queue.append((nx,ny))

def bfs2(idx):
    global answer

    queue=deque()
    dist=[[-1]*N for _ in range(N)]

    # 대륙의 위치들을 큐에 삽입
    for i in range(N):
        for j in range(N):
            if graph[i][j]==idx:
                dist[i][j]=0
                queue.append((i,j))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                # 방문한 적 없는 바다와 만났을 때
                if graph[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    queue.append((nx,ny))
                # 출발지 대륙과는 다른 대륙을 만났을 때
                if graph[nx][ny]>0 and graph[nx][ny]!=idx:
                    answer=min(answer,dist[x][y])
                    return

count=1

# 대륙 번호로 구분
for i in range(N):
    for j in range(N):
        # 대륙이면서 방문하지 않은 곳
        if graph[i][j]>0 and visited[i][j]==0:
            bfs1(i,j)
            count+=1

for i in range(1,count):
    bfs2(i)

print(answer)