N,M=list(map(int,input().split()))

visited=[0]*(N+1)

result=[]

def is_promising():
    base=int(result[0])
    for i in range(1,len(result)):
        if base>int(result[i]): # 오름차순이 아닌 경우
            return False
        else: # 오름차순인 경우
            base=int(result[i]) # 비교값 갱신
            continue
    return True

def BruteForce():
    global result

    if len(result)==M:
        print(' '.join(result))
        return

    for i in range(1,N+1):
        if visited[i]==0:
            result.append(str(i))
            visited[i]=1 
            if is_promising():
                BruteForce()
            result.pop()
            visited[i]=0

BruteForce()

# ------------------------------------------------
# 조합을 이용한 풀이

from itertools import combinations

N,M=list(map(int,input().split()))

case=list(combinations(range(1,N+1),M))

for i in case:
    print(*i)