# 중복 가능
# 오름차순인데 같은 수 가능

# set함수로 중복된 것들을 걸러내줌

N,M=map(int,input().split())

visited=[0]*N

case=list(map(int,input().split())) # 1,7,8,9
case.sort()

result=[]

test=set()

def BruteForce():
    global result

    if len(result)==M:
        test.add(tuple(result))
        return

    for i in range(len(case)):
        if visited[i]==0:
            result.append(case[i])
            visited[i]=1
            BruteForce()
            result.pop()
            visited[i]=0

BruteForce()

test=list(test)
test.sort()

for i in test:
    print(*i)

# --------------------------------------------------------------------
# 순열 이용
# N개의 자연수 중에서 M개를 고름 - nPm 
# 순서가 다르면 다른 것으로 판단 - 순서를 중요 시 - 순열
# 순서가 달라도 같은 것으로 판단 - 순서를 중요 시 안함 - 조합

from itertools import permutations

N,M=map(int,input().split())

case=list(map(int,input().split()))
case.sort()

case2=set(permutations(case,M)) # 순열

case2=list(case2)
case2.sort()

for i in case2:
    print(*i)