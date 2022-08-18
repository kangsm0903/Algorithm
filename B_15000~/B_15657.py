# 중복 가능
# 오름차순인데 같은 수 가능

N,M=map(int,input().split())

case=list(map(int,input().split())) # 1,7,8,9
case.sort()

result=[]

def is_promising():
    base=int(result[0])
    for i in range(1,len(result)):
        if base>int(result[i]): 
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
        result.append(str(case[i]))
        if is_promising():
            BruteForce()
        result.pop()

BruteForce()