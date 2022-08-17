N,M=map(int,input().split())

visited=[0]*N

case=list(map(int,input().split()))
case.sort()

result=[]

def is_promising():
    base=int(result[0])
    for i in range(1,len(result)):
        if base>int(result[i]): # 오름차순이 아니라면
            return False
        else:
            base=int(result[i])
            continue
    return True

def BruteForce():
    global result

    if len(result)==M:
        print(' '.join(result))
        return

    for i in range(len(case)):
        if visited[i]==0:
            result.append(str(case[i]))
            visited[i]=1
            if is_promising():
                BruteForce()
            result.pop()
            visited[i]=0

BruteForce()