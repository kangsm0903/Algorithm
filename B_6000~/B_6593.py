def bfs():
    while queue:
        z,y,x=queue.popleft()

        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            
            # 범위 내에 존재하며,  
            if 0<=nx<X and 0<=ny<Y and 0<=nz<Z:
                if graph[nz][ny][nx]=='.':
                    graph[nz][ny][nx]=graph[z][y][x]+1
                    queue.append((nz,ny,nx))
    return graph[final[0]][final[1]][final[2]]

from collections import deque

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

while True:
    Z,Y,X=map(int,input().split())

    if Z==0 and Y==0 and X==0:
        break

    graph=[]

    for i in range(Z):
        tmp=[]
        for j in range(Y):
            tmp.append(list(map(str,input().rstrip())))
        input()
        graph.append(tmp)

    queue=deque()

    for i in range(Z):
        for j in range(Y):
            for k in range(X):
                if graph[i][j][k]=='S':
                    graph[i][j][k]=0
                    queue.append((i,j,k))
                elif graph[i][j][k]=='E':
                    graph[i][j][k]='.'
                    final=[i,j,k]

    a=bfs()

    if a=='.':
        print("Trapped!")
    else:
        print("Escaped in "+str(a)+" minute(s).")