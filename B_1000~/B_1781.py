# heapq로 구현
# 데드라인 > base의 길이 = 그냥 넣음
# 데드라인 <= base의 길이 = 최솟값을 삭제하고 새로운 값을 넣음 

import heapq
import sys

N=int(sys.stdin.readline())

case=[]

for i in range(N):
    case.append(list(map(int,sys.stdin.readline().split())))

case.sort() # [1,6][1,7][2,4][2,5][3,1][3,2][6,1]

base=[]

for i in range(N):
    if case[i][0] > len(base):
        heapq.heappush(base, case[i][1])
    else:
        heapq.heappush(base,case[i][1])
        heapq.heappop(base)

print(sum(base))

# ------------------------------------------------------------------------------------
# 역 시간 순서로 정렬
# 데드라인이 큰 것부터 받을 수 있는 컵라면이 제일 큰 것을 수행
# 시간초과 이중 for문과 filter로 인한 시간초과 문제발생
import sys

N=int(sys.stdin.readline())

case=[]

for i in range(N):
    case.append(list(map(int,sys.stdin.readline().split())))

case.sort(reverse=True) # [6,1][3,2][3,1][2,5][2,4][1,7][1,6]

deadline=max(case, key=lambda x:x[0])[0]

sub=[]
total=[]

for i in range(deadline,0,-1):
    for k in filter(lambda x:x[0]>=i, case):
        sub.append(k)
    try:
        total.append(max(sub, key=lambda x:x[1])[1])
        case[case.index(max(sub, key=lambda x:x[1]))]=[0,0]
    except ValueError:
        pass
    sub=[]
    

print(sum(total))