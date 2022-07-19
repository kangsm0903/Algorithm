import sys
sys.setrecursionlimit(10**6)

global area

def DFS(x,y):
    global area
    # 범위 넘어가면 False
    if x<0 or y<0 or x>=n or y>=m:
        return False
    # 값이 0이면 False
    if graph[x][y]==0:
        return False
    # 값이 1이면 상하좌우 DFS 실행
    if graph[x][y]==1:
        graph[x][y]=0
        DFS(x+1,y)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x,y-1)
        area+=1
        return True
    return False

n,m=map(int,input().split())

graph=[]

num=0
areas=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        area=0
        if DFS(i,j)==True:
            num+=1
            areas.append(area)

print(num)
if not areas:
    print(0)
else:
    print(max(areas))