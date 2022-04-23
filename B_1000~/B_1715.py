# 각 카드 더미에서 heapq를 이용해 최솟값 2개 뽑은 것을 더함 = A
# 카드 더미에 다시 A를 넣고 위를 반복
import sys
import heapq

N=int(sys.stdin.readline())

case=[]
result=0

for i in range(N):
    case.append(int(sys.stdin.readline()))

heapq.heapify(case)

while len(case)!=1:
    a=heapq.heappop(case)
    b=heapq.heappop(case)
    heapq.heappush(case,a+b)
    result+=a+b

print(result)