# 처음 풀이 pypy로 제출 - python으로 제출 시 시간초과
# 상-하일 때, 좌우로 1,-1씩 | 좌-우일 때, 상하로 1,-1씩 움직이도록 설정했음
# while 문에 이중 for문 때문에 시간초과 나는 것을 추정

import sys
from collections import deque

input=sys.stdin.readline

T=int(input()) # Testcase

for _ in range(T):
    I=int(input()) # 체스판 한 변의 길이

    graph=[[0]*I for _ in range(I)] # I*I판

    queue=deque()

    dx=[-2,2,0,0]
    dy=[0,0,-2,2]

    start=list(map(int,input().split()))
    queue.append(start)

    final=list(map(int,input().split()))

    def bfs():
        if start==final:
            return 0

        while queue:
            x,y=queue.popleft()

            for i in range(4): # 0 1 2 3
                if i<=1: # 상 하
                    for j in range(2,4):
                        nx=x+dx[i]
                        ny=y+(dy[j]//2)

                        if 0<=nx<I and 0<=ny<I:
                            if graph[nx][ny]==0:
                                graph[nx][ny]=graph[x][y]+1
                                queue.append([nx,ny])
                else: # 좌 우 
                    for j in range(0,2):
                        nx=x+(dx[j]//2)
                        ny=y+dy[i]

                        if 0<=nx<I and 0<=ny<I:
                            if graph[nx][ny]==0:
                                graph[nx][ny]=graph[x][y]+1
                                queue.append([nx,ny])
        return graph[final[0]][final[1]]

    print(bfs())

# ------------------------------------------------------------------
# dx, dy를 나이트가 갈 수 있는 모든 경우의 수로 설정해놓았음
# 처음 내 풀이보단 빠름

import sys
from collections import deque

input=sys.stdin.readline

T=int(input()) # Testcase

for _ in range(T):
    I=int(input()) # 체스판 한 변의 길이

    graph=[[0]*I for _ in range(I)] # I*I판

    queue=deque()

    dx=[-2,-2,2,2,-1,1,-1,1]
    dy=[-1,1,-1,1,-2,-2,2,2]

    start=list(map(int,input().split()))
    queue.append(start)

    final=list(map(int,input().split()))

    def bfs():
        if start==final:
            return 0

        while queue:
            x,y=queue.popleft()

            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<I and 0<=ny<I:
                    if graph[nx][ny]==0:
                        graph[nx][ny]=graph[x][y]+1
                        queue.append([nx,ny])
        return graph[final[0]][final[1]]

    print(bfs())