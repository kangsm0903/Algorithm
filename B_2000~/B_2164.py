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

# ------------------------------------------------------------------
# 단일 연결리스트를 통해 Queue 구현 후 풀음

import sys

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class queue():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def size(self):
        return self.length

    def push(self,A):
        new_node=Node(A) # create new_node

        if self.head==None: # if head is not exist, insert new_node
            self.head=new_node
            self.tail=self.head
            self.length+=1
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1

    def pop(self):
        if self.length!=0: # if length is not equal 0, keep going pop method
            node=self.head
            self.head=self.head.next
            self.length-=1
            return node.data
        else:
            return -1

    def empty(self):
        if self.length==0:
            return 1
        else:
            return 0

    def front(self):
        if self.length==0:
            return -1
        else:
            return self.head.data
    
    def back(self):
        if self.length==0:
            return -1
        else:
            return self.tail.data

N=int(sys.stdin.readline())

case=queue()

for i in range(N):
    case.push(i+1) # [1,2,3,4,5,6]

while case.size()!=1:
    case.pop()
    case.push(case.pop())

print(case.front())