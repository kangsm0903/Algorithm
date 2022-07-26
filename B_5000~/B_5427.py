# 61번 줄 visited_human[x][y]+1<visited_fire[nx][ny]
# 상근이의 이동횟수+1이 다음으로 이동하려는 불의 이동횟수보다 작아야함
# 이것 때문에 2시간 날림

from collections import deque
import sys

input=sys.stdin.readline

T=int(input()) # 테스트 케이스

for _ in range(T):
    N,M=map(int,input().split()) # 가로 세로

    graph=[]

    for _ in range(M): 
        graph.append(list(map(str,input().rstrip())))

    visited_fire=[[0]*N for _ in range(M)]
    visited_human=[[0]*N for _ in range(M)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    location_fire=deque()
    location_human=deque()

    for i in range(M):
        for j in range(N):
            if graph[i][j]=='*':
                visited_fire[i][j]=1
                location_fire.append((i,j))
            elif graph[i][j]=='@':
                visited_human[i][j]=1
                location_human.append((i,j))

    def bfs():
        while location_fire: # 불
            x,y=location_fire.popleft()

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<M and 0<=ny<N:
                    # 벽이 아니고, 아직 방문하지 않은 곳이면 불이 번짐
                    if graph[nx][ny]!='#' and visited_fire[nx][ny]==0:
                        visited_fire[nx][ny]=visited_fire[x][y]+1
                        location_fire.append((nx,ny))

        while location_human:
            x,y=location_human.popleft()

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<M and 0<=ny<N:
                    # 빈 공간이며, 아직 방문하지 않은 곳이면
                    if graph[nx][ny]=='.' and visited_human[nx][ny]==0:
                        # 불이 번지지 않은 곳이나 불의 이동횟수<상근이의 이동횟수 라면
                        if visited_fire[x][y]==0 or visited_human[x][y]+1<visited_fire[nx][ny]:
                            visited_human[nx][ny]=visited_human[x][y]+1
                            location_human.append((nx,ny))
                else:
                    return visited_human[x][y]
        return "IMPOSSIBLE"

    print(bfs())