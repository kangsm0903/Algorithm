# 10 10 10 2 1 처럼 현 위치와 목표 위치가 같을 때 result==0으로
# 'Use the stairs'를 출력하게 되는 부분만 고려해줬으면 더 좋았을 듯

# 아예 현 위치와 목표 위치가 같다면 -1을 반환하여
# result가 -1이면 0을 출력하게 해줬음

from collections import deque

F,S,G,U,D=map(int,input().split())

graph=[0]*(F+1)

dx=[U,-D]

queue=deque()
queue.append(S) # 시작지점을 넣어줌

def bfs():
    if S==G:
        return -1

    while queue:
        x=queue.popleft()

        for i in range(2):
            nx=x+dx[i]

            if 0<nx<F+1 and nx!=x:
                if graph[nx]==0:
                    graph[nx]=graph[x]+1
                    queue.append(nx)
    return graph[G]

result=bfs()

if result==-1:
    print(0)
elif result==0:
    print('use the stairs')
else:
    print(result)