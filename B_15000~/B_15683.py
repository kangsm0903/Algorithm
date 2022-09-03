import copy

N,M=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(N)]

# 서, 동, 남, 북
dx=[0,0,-1,1]
dy=[-1,1,0,0]

cctv=[
    [],
    [[0],[1],[2],[3]], # 서 동 남 북
    [[0,1],[2,3]], # 동 서, 남 북
    [[1,3],[1,2],[0,2],[0,3]], # 동 북, 동 남, 서 남, 서 북 
    [[0,1,3],[0,1,2],[0,2,3],[1,2,3]], # 서 동 북, 서 동 남, 남 북 서, 남 북 동
    [[0,1,2,3]] # 동 서 남 북
]

cctv_position=[]
result=[]

for i in range(N):
    for j in range(M):
        if graph[i][j]>0 and graph[i][j]<6:
            cctv_position.append((graph[i][j],i,j)) # (cctv 넘버, x값, y값)

def is_promising(cctv,i,j,sub_graph):
    for k in cctv:
        x=i
        y=j
        while True:
            x=x+dx[k]
            y=y+dy[k]

            if x<0 or y<0 or x>=N or y>=M: # 범위 밖일 경우
                break
            elif sub_graph[x][y]==6: # 벽일 경우 
                break
            else: # 가시거리일 경우 7로 표시
                sub_graph[x][y]=7
    return sub_graph


def dfs(depth, graph):
    global result

    if depth==len(cctv_position): # 종료조건 모든 cctv를 고려했다면 사각지대 계산
        zero_count=70
        count=0
        for i in graph:
            count+=i.count(0)
        zero_count=min(zero_count,count)
        result.append(zero_count)
        return

    sub_graph=copy.deepcopy(graph)
    cctv_num,x,y=cctv_position[depth]

    for i in cctv[cctv_num]:
        is_promising(i,x,y,sub_graph)   
        dfs(depth+1,sub_graph)
        sub_graph=copy.deepcopy(graph)

dfs(0,graph)   

print(min(result))