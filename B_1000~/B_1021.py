# 내 풀이 deque
# deque.rotate(num) : 데크를 num만큼 회전 (양수면 오른쪽, 음수면 왼쪽)

from collections import deque

N,M=map(int,input().split())
dequeue=deque([i for i in range(1,N+1)])
target=list(map(int,input().split()))

count=0

for i in target:
    average_size=len(dequeue)/2
    t=dequeue.index(i) # 1
    if t<=average_size:
        count+=t
        for k in range(t):
            A=dequeue.popleft()
            dequeue.append(A)
        dequeue.popleft()
    else:
        count+=(len(dequeue)-t)
        for k in range(len(dequeue)-t):
            B=dequeue.pop()
            dequeue.appendleft(B)
        dequeue.popleft()

print(count)

# ----------------------------------------------------------------------------
# deque rotate 사용한 다른 사람 풀이

N,M=map(int, input().split())
A=list(map(int,input().split())) # target
B=deque([i+1 for i in range(N)])

a=0

for i in A:
    while True:
        if i==B[0]: # deque의 0번 인덱스가 target과 같다면 popleft 후 break
            B.popleft()
            break
        elif B.index(i) <= len(B)//2:
            B.rotate(-1) 
            a+=1
        elif B.index(i) > len(B)//2:
            B.rotate(1)
            a+=1

print(a)