# 비내림차순
# N개에서 M개를 고른 수열

N,M=map(int,input().split())

case=list(map(int,input().split()))

visited=[0]*N

result=[]
test=set()

def is_promising():
    base=result[0]
    for i in range(len(result)):
        if base>result[i]: # 오름차순이 아니라면
            return False
        else:
            base=result[i]
            continue
    return True

def BruteForce():
    global result
    
    if len(result)==M:
        test.add(tuple(result))
        return

    for i in range(len(case)):
        if visited[i]==0:
            visited[i]=1
            result.append(case[i])
            if is_promising():
                BruteForce()
            visited[i]=0
            result.pop()

BruteForce()

test=list(test)
test.sort()

for i in test:
    print(*i)

# ------------------------------------------------------------------------------------------------

# 조합을 이용한 풀이
# 오름차순이기에 (7,9)(9,7)에서 후자는 필요가 없기에 조합을 이용해서 (7,9)만 씀

from itertools import combinations

N,M=map(int,input().split())

case=list(map(int,input().split()))
case.sort()

result=set(combinations(case,M))
result=list(result)
result.sort()


for i in result:
    print(*i)