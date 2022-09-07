# 스티커를 회전시키지 않고 모눈종이에서 떼어낸다.

# 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 스티커를 붙일 수 있는 위치를 찾는다.
# 위쪽의 왼쪽부터 스티커를 붙이기 시작한다.

# 선택한 위치에 스티커를 붙인다.
# 붙일 수 있는 위치가 전혀 없다면 시계방향으로 90도 회전한 뒤 2번을 반복한다.

# 네 번 반복해서 0도, 90도, 180도, 270도 회전시켜보고 붙이지 못한다면 붙이지 않고 버린다.

import copy
import sys

n,m,k=map(int,input().split()) # 세로 가로 스티커 갯수

stickers=[]
graph=[[0]*m for _ in range(n)] # 스티커 붙일 스케치북(graph)

for i in range(k):
    x,y=map(int,input().split()) # 스티커 크기
    # 스티커 정보
    stickers.append((x,y,[list(map(int,input().split())) for _ in range(x)])) 


# 시벌탱 이부분이 문제임
def is_promising(x,y,sticker, graph):
    # 회전한 현재의 스티커가 graph에 붙일 수 있는 공간이 있는 지 확인
    for i in range(len(sticker)): 
        for j in range(len(sticker[0])): 
            if graph[x+i][y+j]==1 and sticker[i][j]==1: # 스케치북에 이미 스티커가 붙어있거나 && 스티커의 [x][y]위치에 겹치는 부분이 있거나 
                return False
        
    for i in range(len(sticker)):
        for j in range(len(sticker[0])): 
            if sticker[i][j]==1: # 
                graph[x+i][y+j]=1

    return True





def dfs(depth,graph):
    global result

    if depth==len(stickers): # 종료조건
        count=0
        compare=0
        for i in graph:
            # graph의 1을 카운트하여 최댓값을 구하고 result에 때려넣어 최종 최댓값을 도출
            count+=i.count(1)
        compare=max(compare,count)
        result.append(compare)
        return

     # depth에 해당되는 스티커 하나 할당
    sticker=stickers[depth] # (x값,y값,스티커 정보)

    # 0도 일때, is_promising을 돌림
    new_sticker=sticker[2]
    sub_graph=copy.deepcopy(graph)

    for i in range(n-len(new_sticker),-1,-1):
        for j in range(m-len(new_sticker[0]),-1,-1):
            # i,j는 스케치북의 위치 / 회전한 스티커 / 최근 스케치북
            if is_promising(i,j,new_sticker, sub_graph): # is_promising이 참이면 
                dfs(depth+1,sub_graph)
            else: # 거짓이라면 그냥 continue
                sub_graph=copy.deepcopy(graph)
                continue

    # 0도 90도 180도 270도 회전
    for _ in range(3): 
        # 스티커를 돌리기 위해 x*y인 스티커를 y*x크기의 스케치북(graph)로 변경
        new_sticker=[[0]*sticker[0] for _ in range(sticker[1])] 

        # -90도씩 회전
        for x in range(sticker[0]): # x값
            for y in range(sticker[1]): # y값
                new_sticker[len(new_sticker)-1-y][x]=sticker[2][x][y] # B[x][y]=A[A행-1-y][x]

        sub_graph=copy.deepcopy(graph)

        for i in range(n-len(new_sticker),-1,-1):
            for j in range(m-len(new_sticker[0]),-1,-1):
                # i,j는 스케치북의 위치 / 회전한 스티커 / 최근 스케치북
                if is_promising(i,j,new_sticker, sub_graph): # is_promising이 참이면 
                    dfs(depth+1,sub_graph)
                else: # 거짓이라면 sticker값을 갱신 후 continue
                    # sticker=(len(new_sticker),len(new_sticker[0]),new_sticker)
                    # breaker=True
                    # break
                    sub_graph=copy.deepcopy(graph)
                    continue
        
        sticker=(len(new_sticker),len(new_sticker[0]),new_sticker)

    # 아예 스티커를 붙일 수 없다면 그냥 다음 스티커로 넘어감
    sub_graph=copy.deepcopy(graph)
    dfs(depth+1,sub_graph)

        # 회전시키고 is_promising 함수 고고
        # 넣을 수 있다면 dfs(depth+1,graph)
        # 넣을 수 없다면 continue로 다음 회전을 진행
        # 다 돌려도 넣을 수 없다면 다음 스티커로 넘김
        
result=[]
dfs(0,graph)

print(result[0])