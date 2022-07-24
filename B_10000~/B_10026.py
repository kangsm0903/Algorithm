import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y):
    # 현재 색상 좌표를 방문한다.
    visited[x][y]=True
    current_color=graph[x][y]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            # 현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            # 방문하지 않았다면
            if visited[nx][ny]==False:
                # 현재 색상과 좌표의 색상이 같다면
                if graph[nx][ny]==current_color:
                    dfs(nx,ny)

n=int(input().rstrip())

graph=[list(input().rstrip()) for _ in range(n)]

visited=[[False]*n for _ in range(n)]

color_cnt, blind_cnt=0,0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            dfs(i,j)
            color_cnt+=1

for i in range(n):
    for j in range(n):
        if graph[i][j]=='R':
            graph[i][j]='G'

visited=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):  
        if visited[i][j]==False:
            dfs(i,j)
            blind_cnt+=1

print(color_cnt, blind_cnt)