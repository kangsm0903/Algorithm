# 3273 - 이진탐색 구현
# 아래의 코드보다 이진탐색 코드가 더 빠를 거 같은데 왜 더 느린지 모르겠음
# 607ms
import sys

a=int(sys.stdin.readline()) # 100,000 10만

case=list(map(int,sys.stdin.readline().split())) #[5,12,7,10,9,1,2,3,11]

case.sort()

x=int(sys.stdin.readline()) # 2,000,000 

count=0

def BinarySearch(target,arr,first,last):
    global count
    mid = (first+last)//2

    if mid<first or mid>last:
        return 0

    if arr[mid]==target:
        count+=1
    elif arr[mid] > target:
        return BinarySearch(target,arr,first,mid-1)
    elif arr[mid] < target:
        return BinarySearch(target,arr,mid+1,last)

for i in case:
    BinarySearch(x-i,case,0,len(case)-1)

print(count//2)

# --------------------------------------------------------------------
# 140ms
a=int(sys.stdin.readline())
case=list(map(int,sys.stdin.readline().split()))
b=int(sys.stdin.readline())

case.sort()

count=0

l,r=0,a-1
while l != r:
    if case[l]+case[r]==b:
        count+=1
        l+=1
    elif case[l]+case[r]>b:
        r-=1
    else: # case[1]+case[r]<b
        l+=1
print(count)