# 보석의 무게의 최솟값 기준으로 value에 가격들을 음수로 넣어줌
# 음수인 가격들의 최솟값(-99,-65)중 제일 최솟값을 heapq로 total에 부호바꿔서 더해줌
# 이것을 가방의 갯수만큼 반복
import sys
import heapq

N,K = map(int, sys.stdin.readline().split())
jew=[]
for i in range(N): # 보석 무게, 보석 가치
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))

bags=[]
for i in range(K):
    bags.append(int(sys.stdin.readline()))

bags.sort()

value=[]
total=0

for bag in bags:
    while jew and bag >= jew[0][0]: # 보석의 무게가 같거나 작을 때 넣음
        heapq.heappush(value, -heapq.heappop(jew)[1])
    if value:
        total-=heapq.heappop(value)
    else:
        pass

print(total)