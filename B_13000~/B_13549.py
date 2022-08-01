# 33번 줄에 방문했던 곳을 갔을 때, 기존과 새로운 것을 비교하여 더 작은 것으로 갱신해준다.

from collections import deque

N,M=map(int,input().split()) # 수빈, 동생

visited=[-1]*100001
visited[N]=0 # 수빈이 위치를 0으로 설정

def bfs():
    queue=deque()
    queue.append(N) # 수빈이 위치를 할당

    while queue:
        x=queue.popleft()
        # dx=[x+1,x-1,2*x] 
        dx=[2*x,x+1,x-1]

        if x==M:
            return visited[x]

        for i in range(3):
            nx=dx[i]
            # 반례 4,6
            # 범위 내이며 방문하지 않았을 때
            if 0<=nx<100001 and visited[nx]==-1:
                if i==0: # 2*x라면 0초 소모
                    visited[nx]=visited[x]
                    queue.append(nx)
                else: # i==0 or 1이라면 1초 소모
                    visited[nx]=visited[x]+1
                    queue.append(nx)

            # 범위 내이며 방문했었다면
            # visited[nx]는 기존 꺼 visited[x] 새로운거
            if 0<=nx<100001 and visited[nx]!=-1:
                if i==0 and visited[nx]>visited[x]:
                    visited[nx]=visited[x]
                    queue.append(nx)
                if i!=0 and visited[nx]>visited[x]:
                    visited[nx]=visited[x]+1
                    queue.append(nx)

print(bfs())

 # if 0<=nx<100001:
            #     if i==0:
            #         if visited[nx]==0: # 방문하지 않았다면
            #             visited[nx]=visited[x]
            #             queue.append(nx)
            #         else: # 방문했다면
            #             if visited[nx]>
            #     else:
            #         pass