# dfs

def dfs(x,y):
    global cnt
    if x<0 or y<0 or x>=N or y>=N:
        return False

    if graph[x][y]==1:
        graph[x][y]='T'
        cnt+=1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

N=int(input()) # 7

graph=[]

for i in range(N):
    graph.append(list(map(int,input())))

result=0
count=[]

for i in range(N):
    for j in range(N):
        cnt=0
        if dfs(i,j)==True:
            result+=1
            count.append(cnt)

print(result)
count.sort()
for i in count:
    print(i)