from collections import deque

n,m=map(int,input().split()) # 5,6

graph=[]

dx=[-1,1,0,0] # 상 하
dy=[0,0,-1,1] # 좌 우

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    queue=deque([])
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 범위 초과
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 벽에 부딪혔을 때
            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))