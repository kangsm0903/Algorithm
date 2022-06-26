# dequeue

from collections import deque

n=int(input())

for i in range(n):
    target=list(input()) # <<BP<A>>Cd-

    dequeue1=deque([])
    dequeue2=deque([])

    for k in target:
        if k=='<':
            if dequeue1:
                dequeue2.appendleft(dequeue1.pop())
        
        elif k=='>':
            if dequeue2:
                dequeue1.append(dequeue2.popleft())

        elif k=='-':
            if dequeue1:
                dequeue1.pop()

        else:
            dequeue1.append(k)

    result=dequeue1+dequeue2
    print(''.join(result))

# ---------------------------------------------------------------------------------
# stack
n=int(input())

for i in range(n):
    target=list(input()) # <<BP<A>>Cd-

    stack1=[]
    stack2=[]

    for k in target:
        if k=='<':
            if stack1:
                stack2.append(stack1.pop())
            
        elif k=='>':
            if stack2:
                stack1.append(stack2.pop())
        
        elif k=='-':
            if stack1:
                stack1.pop()
        
        else:
            stack1.append(k)

    stack1.extend(reversed(stack2))

    print(''.join(stack1))