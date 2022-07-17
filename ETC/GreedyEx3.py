from collections import deque

N=int(input())

case=sorted(list(map(int,input().split())),reverse=True)

case=deque(case)

breaker=False

cnt=0

for i in range(len(case)):
    test=[]
    for k in range(case[0]):
        test.append(case.popleft())
    
    if max(test) == len(test):
        pass
    else:
        test=[]

    if test:
        cnt+=1

    if len(case)==0 or max(case)>len(case):
        break

print(cnt)

# -------------------------------------------------------------------------
# 오름차순 정렬 이후 공포도가 가장 낮은 모험가부터 하나씩 확인

n=int(input())
data=list(map(int,input().split()))
data.sort()

result=0 # Count group
count=0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count+=1
    if count>=i: # 그룹 결성
        result+=1
        count=0

print(result)