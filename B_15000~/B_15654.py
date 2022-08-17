N,M=map(int,input().split())

visited=[0]*N

case=list(map(int,input().split()))
case.sort()

result=[]

def BruteForce():
    global result

    if len(result)==M:
        print(' '.join(result))
        return

    for i in range(len(case)):
        if visited[i]==0:
            result.append(str(case[i]))
            visited[i]=1
            BruteForce()
            result.pop()
            visited[i]=0

BruteForce()