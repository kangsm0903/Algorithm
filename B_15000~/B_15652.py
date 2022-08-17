# 중복 허용
# 비내림차순

N,M=list(map(int,input().split()))

result=[]

def is_promising():
    base=int(result[0])
    for i in range(1,len(result)):
        if base>int(result[i]): # 비내림차순이 아닐 때
            return False
        else:
            base=int(result[i]) # 비교값을 최신으로 갱신
            continue
    return True

def BruteForce():
    global result

    if len(result)==M:
        print(' '.join(result))
        return

    for i in range(1,N+1):
        result.append(str(i))
        if is_promising():
            BruteForce()
        result.pop()

BruteForce()