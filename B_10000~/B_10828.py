# Stack
import sys

N=int(sys.stdin.readline())

case=[]

def push(arr,x):
    arr.insert(0,x)

def pop(arr):
    if len(arr)==0:
        print(-1)
    else:
        item=arr[0]
        del arr[0]
        print(item)

def size(arr):
    print(len(arr))

def empty(arr):
    if len(arr)==0:
        print(1)
    else:
        print(0)

def top(arr):
    if len(arr)==0:
        print(-1)
    else:
        print(arr[0])   

for i in range(N):
    command=list(map(str,sys.stdin.readline().split()))
    if len(command)==2:
        push(case,command[1])
    elif command[0]=='top':
        top(case)
    elif command[0]=='size':
        size(case)
    elif command[0]=='empty':
        empty(case)
    else:
        pop(case)