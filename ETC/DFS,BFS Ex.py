def dfs(x,y):
    if x<0 or y<0 or x>=N or y>=M:
        return False

    # 방문 처리
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

N,M=map(int,input().split())

graph=[]
result=0

for i in range(N):
    graph.append(list(map(int,input())))

for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            result+=1

print(result)

# ------------------------------------------------------------------

N,M=map(int,input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int,input())))

cnt=0

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if graph[x][y]==0:
        graph[x][y]=1 # 방문처리
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            cnt+=1
print(cnt)