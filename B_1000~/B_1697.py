from collections import deque

N,K=map(int,input().split()) # N - 수빈이 위치 / K - 동생 위치

road=[0 for _ in range(100001)]

queue=deque([])
queue.append(N)

road[N]=1

dx=[-1,1] # x-1 / x+1

def bfs():
    if N==K:
        return 0
    while queue:
        x=queue.popleft()

        for i in (x-1,x+1,x*2):
            nx=i

            if 0<=nx<=100000 and road[nx]==0:
                if nx==K:
                    road[nx]=road[x]+1
                    return road[nx]-1
                road[nx]=road[x]+1
                queue.append(nx)

print(bfs())

# ---------------------------------------------------
# 비슷비슷함

def bfs():
    queue=deque([])
    queue.append(n)

    while queue:
        x=queue.popleft()

        if x==k:
            print(case[x])
            break

        for i in (x-1,x+1,x*2):
            if 0<=i<=100000 and case[i]==0:
                case[i]=case[x]+1
                queue.append(i)

n,k=map(int,input().split())
case=[0]*100001

bfs()