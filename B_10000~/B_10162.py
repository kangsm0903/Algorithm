# 마지막 10초일때 나머지가 존재하면 3개의 버튼으로 T초를 맞출 수 없는 것이기에 -1 출력
import sys

T=int(sys.stdin.readline())

case=[300,60,10]

result=[]

for i in case:
    if i==10 and T%i>0:
        result=-1
    elif T//i==0:
        result.append(T//i)
    else:
        result.append(T//i)
        T=T%i

if result==-1:
    print(result)
else:
    for i in result:
        print(i, end=' ')