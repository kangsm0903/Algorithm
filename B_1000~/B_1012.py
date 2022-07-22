# DFS
import sys
sys.setrecursionlimit(10**6)

T=int(input())

def bfs(x,y):
    # 범위 넘어가면 넘김
    if x<0 or y<0 or x>=M or y>=N:
        return False

    if graph[x][y]==1:
        graph[x][y]=2
        bfs(x-1,y)
        bfs(x+1,y)
        bfs(x,y-1)
        bfs(x,y+1)
        return True
    return False

for _ in range(T):
    result=0
    M,N,K=map(int,input().split())

    graph=[[0]*N for _ in range(M)]

    for i in range(K):
        A,B=map(int,input().split())
        graph[A][B]=1

    for i in range(M):
        for j in range(N):
            if bfs(i,j)==True:
                result+=1

    print(result)
        