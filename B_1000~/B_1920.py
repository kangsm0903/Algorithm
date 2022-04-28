# Binary Search

import sys

N=int(sys.stdin.readline())

case=list(map(int,sys.stdin.readline().split()))
case.sort() # 오름차순 1 2 3 4 5

M=int(sys.stdin.readline())

case2=list(map(int,sys.stdin.readline().split()))

def Binary_Search(arr,value):
    start=0
    end=len(arr)
    while True:
        mid=(start+end)//2
        if start>=end:
            print(0)
            break
        elif arr[mid]==value:
            print(1)
            break
        elif arr[mid]<value:
            start=mid+1
        elif arr[mid]>value:
            end=mid

for i in case2:
    Binary_Search(case,i)
