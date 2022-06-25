import sys

target=list(map(str,sys.stdin.readline().strip("\n"))) # abcd 커서가 존재할 수 있는 위치는 5곳
target2=[]

n=int(sys.stdin.readline())

for i in range(n):
    command=list(map(str,sys.stdin.readline().strip("\n")))

    if command[0]=='L': # 왼쪽으로 1칸 이동
        if len(target)==0:
            continue
        target2.append(target.pop()) # target2에 target의 마지막 원소 삽입

    elif command[0]=='D': # 오른쪽으로 1칸 이동
        if len(target2)==0:
            continue
        target.append(target2.pop()) # target에 target2의 마지막 원소 삽입

    elif command[0]=='B': # 커서 왼쪽의 문자 삭제
        if len(target)==0:
            continue
        target.pop()

    else: # 삽입
        target.append(command[2])

target.extend(reversed(target2))

print(''.join(target))


#----------------------------------------------------------------------------------------


from collections import deque

dequeue=deque(input())
queue=deque([])

n=int(input())

for i in range(n):
    command=list(input().split())

    if command[0]=='P': # 추가
        dequeue.append(command[1])
    
    elif command[0]=='B': # 삭제
        if dequeue:
            dequeue.pop()

    elif command[0]=='L': # << 이동
        if dequeue:
            queue.appendleft(dequeue.pop())

    elif command[0]=='D':
        if queue:
            dequeue.append(queue.popleft())

result=dequeue+queue