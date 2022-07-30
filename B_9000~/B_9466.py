import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result

    visited[x]=True # 방문 확인
    number=case[x]
    cycle.append(x)

    if visited[number]:
        if number in cycle:
            result+=cycle[cycle.index(number):]
            return
    else:
        dfs(number)

T=int(input())

for _ in range(T):
    N=int(input())

    case=[0]+list(map(int,input().split()))

    visited=[True]+[False]*N

    result=[]

    for i in range(1,N+1):
        cycle=[]
        if visited[i]==False:
            dfs(i)
        
    print(N-len(result))