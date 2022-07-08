# singly linked list

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

Queue=queue()

N=int(sys.stdin.readline())

for i in range(N):
    case=list(map(str, sys.stdin.readline().split()))
    
    if case[0]=="push":
        Queue.push(case[1])
    elif case[0]=="pop":
        print(Queue.pop())
    elif case[0]=="size":
        print(Queue.size())
    elif case[0]=="empty":
        print(Queue.empty())
    elif case[0]=="front":
        print(Queue.front())
    elif case[0]=="back":
        print(Queue.back())

# -------------------------------------------------------------------------------------

# deque 

import sys
from collections import deque

dequeue=deque()

N=int(sys.stdin.readline())

for i in range(N):
    case=list(map(str,sys.stdin.readline().split()))

    if case[0]=="push":
        dequeue.append(case[1])
    elif case[0]=="pop":
        if len(dequeue)==0:
            print(-1)
        else:
            print(dequeue.popleft())
    elif case[0]=="size":
        print(len(dequeue))
    elif case[0]=="empty":
        if len(dequeue)==0:
            print(1)
        else:
            print(0)
    elif case[0]=="front":
        if len(dequeue)==0:
            print(-1)
        else:
            print(dequeue[0])
    elif case[0]=="back":
        if len(dequeue)==0:
            print(-1)
        else:
            print(dequeue[-1])