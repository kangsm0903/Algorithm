from collections import deque

N,M=map(int,input().split())

visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1 # 시작 지점

graph=[]

for i in range(N):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,z):
    queue=deque()
    queue.append((x,y,z))

    while queue:
        a,b,c=queue.popleft()

        if a==N-1 and b==M-1:
            return visited[a][b][c]

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]

            # 범위를 벗어나면 continue
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            # 다음 이동할 곳이 벽이며, 벽 파괴 기회를 사용하지 않은 경우
            # 다음 이동할 곳이 벽이며, 벽 파괴 기회가 없다면 그냥 무시
            if graph[nx][ny]==1 and c==0:
                visited[nx][ny][1]=visited[a][b][0]+1
                queue.append((nx,ny,1))
            # 다음 이동할 곳이 벽이 아니며, 아직 한 번도 방문하지 않은 곳인 경우
            # 다음 이동할 곳이 벽이 아니며, 방문한 곳이라면 무시
            if graph[nx][ny]==0 and visited[nx][ny][c]==0:
                visited[nx][ny][c]=visited[a][b][c]+1
                queue.append((nx,ny,c))

    return -1


print(bfs(0,0,0))