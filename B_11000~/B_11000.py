# 1. 입력값을 받음 리스트속 리스트로
# 2. 첫번째 끝나는 시간을 할당하고 == last last보다 크거나 같은 것을 선택 후 다시 last에 할당
# 3. 할당한 것들을 삭제함 - 강의실 1개
# 4. 남아있는 것중 첫번째 강의실의 끝나는 시간을 last에 할당 후 2번 반복 
# 5. 리스트가 다 없어질 때까지 반복
# -----------------------------------------------------------------------------------
# 시간초과 실패 
import sys
from typing import Type

N=int(sys.stdin.readline())

case=[]

for i in range(N):
    case.append(list(map(int, sys.stdin.readline().split())))

case.sort() # [[1,3][2,4][3,5]]

last=case[0][1] # 첫번째 마감 시간
case.remove(case[0])

count=0

breaker=False

while True:
    for i in case:
        if case.count("0")==(N-1):
                breaker=True
                break
        elif last <= i[0]: # last보다 크거나 같으면 last에 그 값을 할당하고 그 케이스 없앰
            last=i[1]
            case[case.index(i)]="0"
        else: # last보다 작으면 넘기고 for루프가 한번 끝날 때마다 +1
            pass
    count+=1
    last=0
    if breaker==True:
        break

print(count)