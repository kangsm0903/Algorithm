# deque 앞의 원소, 뒤의 원소 둘 다 접근 가능한 자료구조

import sys

N=int(sys.stdin.readline())

case=[]

def push_front(arr,x):
    arr.insert(0,x)

def push_back(arr,x): # 맨 뒤에 삽입
    arr.append(x)

def pop_front(arr):
    if len(arr)==0:
        print(-1)
    else:
        item=arr[0]
        del arr[0]
        print(item)

def pop_back(arr):
    if len(arr)==0: # 정수 없다면 -1
        print(-1)
    else:
        item=arr[-1]
        del arr[-1]
        print(item)

def size(arr):
    print(len(arr))

def empty(arr):
    if len(arr)==0:
        print(1)
    else:
        print(0)

def front(arr): # 맨 앞 정수 출력
    if len(arr)==0:
        print(-1)
    else:
        print(arr[0])

def back(arr): # 맨 뒤 정수 출력
    if len(arr)==0:
        print(-1)
    else:
        print(arr[-1])

for i in range(N):
    command=list(map(str,sys.stdin.readline().split()))
    if len(command)==2:
        if command[0]=="push_back":
            push_back(case,command[1])
        else:
            push_front(case,command[1])
    elif command[0]=='front':
        front(case)
    elif command[0]=='back':
        back(case)
    elif command[0]=='size':
        size(case)
    elif command[0]=='empty':
        empty(case)
    elif command[0]=='pop_front':
        pop_front(case)
    elif command[0]=='pop_back':
        pop_back(case)