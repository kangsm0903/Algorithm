# deque 데이터를 처리할 수 있는 양방향 자료구조 - 앞,뒤 양쪽 방향에서 엘리먼트를 추가하거나 제거할 수 있음
# 스택처럼 써도 되고 큐처럼 써도됨
# deque는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠름
# list가 양 끝 엘리먼트에 접근하여 삽입 제거 - O(n)
# deque가 양 끝 엘리먼트에 접근하여 삽입 제거 - O(1)

# 가장 큰 수와 작은 수를 먼저 할당 후 기존 리스트에서 제거
# 남은 수들 중 가장 큰 수와 작은 수, 할당한 리스트 속 큰 수와 작은 수의 차들 중 절댓값이 가장 큰 것을 할당
# 이를 반복
import sys
from collections import deque

N=int(sys.stdin.readline())

case=list(map(int,sys.stdin.readline().split()))
case.sort()

case=deque(case)

total=deque()
total.appendleft(deque.popleft(case))
total.append(deque.pop(case)) # 처음에 가장 큰 수와 가장 작은 수를 total에 할당
# total=[1,20]
count=abs(total[0]-total[1]) # 두 수의 차를 count에 더해줌


for i in range(N-2):# 0 1 2
    test1=abs(total[0]-case[0]) # total의 최솟값 - 기존 리스트의 최솟값
    test2=abs(total[-1]-case[0]) # total의 최댓값 - 기존 리스트의 최솟값
    test3=abs(total[0]-case[-1]) # total의 최솟값 - 기존 리스트의 최댓값
    test4=abs(total[-1]-case[-1]) # total의 최댓값 - 기존 리스트의 최댓값
    count+=max(test1,test2,test3,test4)

    # 각각의 경우일 때 total에 넣는 위치가 달라짐
    if max(test1,test2,test3,test4)==test1: 
        total.appendleft(deque.popleft(case)) # test1은 기존 리스트의 왼쪽 원소를 뽑고 total의 왼쪽에 넣음
    elif max(test1,test2,test3,test4)==test2:
        total.append(deque.popleft(case)) # test2는 기존 리스트의 왼쪽 원소를 뽑고 total의 오른쪽에 넣음
    elif max(test1,test2,test3,test4)==test3:
        total.appendleft(deque.pop(case)) # test3는 기존 리스트의 오른쪽 원소를 뽑고 total의 왼쪽에 넣음
    else:
        total.append(deque.pop(case)) # test4는 기존 리스트의 오른쪽 원소를 뽑고 total의 오른쪽에 넣음

print(count)