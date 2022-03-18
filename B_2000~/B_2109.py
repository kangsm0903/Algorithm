# 0<=N<=10,000 / 1<=d<=10,000 이중 for문과 filter함수로 시간초과 나는 것으로 보임
import sys

N=int(sys.stdin.readline())

case=[]
total=0

for i in range(N):
    case.append(list(map(int, sys.stdin.readline().split()))) # [돈, 남은 일자]

day=max(case,key=lambda x:x[1])[1] # 20

sub=[]

for i in range(day,0,-1):
    for k in filter(lambda x:x[1]>=i, case):
        sub.append(k)
    try:
        total+=max(sub,key=lambda x:x[0])[0]
        case[case.index(max(sub,key=lambda x:x[0]))]=[0,0]
    except ValueError:
        pass
    sub=[]

print(total)