# 시간초과

import sys

N=int(sys.stdin.readline())

case=list(map(int,sys.stdin.readline().split()))

case.sort()

total=0
totalcase=[]

totalcase.append(case[0])
totalcase.append(case[-1])
total+=abs(case[0]-case[-1])
case.remove(case[0])
case.remove(case[-1])

def front(i):
    global total
    totalcase.append(case[i])
    total+=abs(totalcase[-2]-totalcase[-1])

def back(i):
    global total
    totalcase.insert(0,case[i])
    total+=abs(totalcase[0]-totalcase[1])

for i in range(len(case)//2): # case=[4 8 10 15]
    if abs(totalcase[0]-case[i]) < abs(totalcase[-1]-case[i]):
        front(i)
    else:
        back(i)

    if abs(totalcase[0]-case[-i-1]) < abs(totalcase[-1]-case[-i-1]):
        front(-i-1)
    else:
        back(-i-1)

print(total)