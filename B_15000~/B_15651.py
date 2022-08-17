N,M=list(map(int,input().split()))

visited=[0]*(N+1)

result=[]

def BruteForce():
    global result

    if len(result)==M:
        print(' '.join(result))
        return

    for i in range(1,N+1):
        result.append(str(i))
        BruteForce()
        result.pop()

BruteForce()