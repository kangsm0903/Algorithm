# 제일 위의 카드를 버린다.
#   제일 위의 카드를 뽑기 위해 pop(0)을 하면 O(N) 복잡도가 걸리기에
#   deque 양방향 큐를 써서 O(1) 복잡도로 상단 카드를 뽑았다.

# 그 다음 위의 카드를 아래로 내린다.
#   그 다음 위의 카드 또한 deque로 O(1) 복잡도로 꺼내고 
#   append() 맨 뒤 삽입은 복잡도가 O(1)이기에 그냥 넣어준다.

from collections import deque
import sys

N=int(sys.stdin.readline())

case=deque()

for i in range(1,N+1):
    case.append(i)

for i in range(N-1):
    case.popleft()
    item=case.popleft()
    case.append(item)

print(case[0])