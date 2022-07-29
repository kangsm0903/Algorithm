from collections import deque

N,M=map(int,input().split())

visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1 # 시작지점 - 안 부수고 가는 경우

graph=[]

for i in range(N):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
queue.append((0,0,0))

def bfs():
    # z축 1: 벽을 부수고 가는 경우 / 0: 부수지 않고 가는 경우 
    while queue:
        x,y,z=queue.popleft()

        if x==N-1 and y==M-1:
            return visited[x][y][z]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                # 다음 이동이 벽이며, 벽 파괴 기회가 있는 경우
                # 벽 부수고 이동하고 z축을 1로 변경 (부수지 않는 경우 -> 벽을 부수고 가는 경우로 변경)
                if graph[nx][ny]==1 and z==0:
                    visited[nx][ny][1]=visited[x][y][0]+1 # 벽을 부숴야하기에 z축에 현재상태+1
                    queue.append((nx,ny,1)) # 부순 경우를 큐에 push
                
                # 다음 이동이 벽이 아니며, 한 번도 방문하지 않을 곳인 경우
                # 벽 안 부수고 이동, 한 번도 방문하지 않음==z축이 0임을 뜻함
                if graph[nx][ny]==0 and visited[nx][ny][z]==0:
                    visited[nx][ny][z]=visited[x][y][z]+1
                    queue.append((nx,ny,z))
    return -1

print(bfs())