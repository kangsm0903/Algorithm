# heapq
import sys
import heapq

N=int(sys.stdin.readline())

case=[]

for i in range(N):
    case.append(list(map(int,sys.stdin.readline().split()))) # [p,d] [돈, 날짜]

case.sort(key=lambda x:x[1])

print(case) # [[20, 1], [2, 1], [100, 2], [8, 2], [10, 3], [50, 10], [5, 20]]

heaps=[]

heapq.heapify(heaps)

for pay, day in case: # pay, day를 구분
    heapq.heappush(heaps, pay) # heaps에 pay 값들을 넣음

    if day < len(heaps): # 만약에 day=2인데 heaps에 값이 3개다(2일차 이하의 돈 목록들이 3개라는 것)
        heapq.heappop(heaps) # 2일차 이하의 돈 3개 중 최솟값을 없앰
    
print(sum(heaps))

# ----------------------------------------------------------------------------------

# 0<=N<=10,000 / 1<=d<=10,000 이중 for문과 filter함수로 시간초과 나는 것으로 보임
import sys

N=int(sys.stdin.readline())

case=[]
total=0

for i in range(N):
    case.append(list(map(int, sys.stdin.readline().split()))) # [돈, 남은 일자]

day=max(case,key=lambda x:x[1])[1] # 20

sub=[]

for i in range(day,0,-1):
    for k in filter(lambda x:x[1]>=i, case):
        sub.append(k)
    try:
        total+=max(sub,key=lambda x:x[0])[0]
        case[case.index(max(sub,key=lambda x:x[0]))]=[0,0]
    except ValueError:
        pass
    sub=[]

print(total)