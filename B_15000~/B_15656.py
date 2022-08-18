N,M=map(int,input().split())

case=list(map(int,input().split())) # 1,7,8,9
case.sort()

result=[]

def BruteForce():
    global result

    if len(result)==M:
        print(' '.join(result))
        return

    for i in range(len(case)):
        result.append(str(case[i]))
        BruteForce()
        result.pop()

BruteForce()