from collections import deque

N,M=map(int,input().split())

graph=[]

dx=[-1,1,0,0] # 상 하 방향 벡터
dy=[0,0,-1,1] # 좌 우 방향 벡터

for i in range(N):
    graph.append(list(map(int,input())))

def BFS(x,y):
    queue=deque([])
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 범위 초과
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue

            # 벽에 부딪혔을 때
            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    return graph[N-1][M-1]

print(BFS(0,0))