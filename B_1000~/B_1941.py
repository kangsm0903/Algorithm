# 나누기와 나머지를 이용해서 숫자 하나만으로 좌표를 표현할 수 있음
# x=i//5 , y=i%5

def dfs(picked,S,Y):
    global result,graph,dx,dy

    if Y>=4: # Y의 갯수가 4이상이면 반환
        return

    if len(picked)==7 and S>=4: # S가 4개이상이고 갯수가 7개이면
        picked=tuple(sorted(picked)) # 정렬해주고
        if picked not in result: # result에 중복되는 것이 없으면 넣어줌
            result.add(picked)
        return

    for i in picked: # 특정 부분의 상하좌우 모두를 탐색해봄
        x=i//5 # 앞부분 숫자 하나만으로 좌표를 표현할 수 있음
        y=i%5  # 뒷부분

        for j in range(4): # 상하좌우
            nx=x+dx[j]
            ny=y+dy[j]

            position=nx*5+ny # 좌표 

            if 0<=nx<5 and 0<=ny<5 and position not in picked: # 범위 내이면
                picked.append(position) # 좌표를 picked에 삽입
                if graph[nx][ny]=='S':
                    dfs(picked,S+1,Y)
                else:
                    dfs(picked,S,Y+1)
                picked.pop()

graph=[input() for _ in range(5)]

result=set()

dy=[1,-1,0,0]
dx=[0,0,1,-1]

for i in range(5):
    for j in range(5):
        if graph[i][j]=='S':
            picked=[]
            picked.append(i*5+j)
            dfs(picked,1,0)

print(len(result))