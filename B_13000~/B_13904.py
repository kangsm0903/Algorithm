# 아이디어만 참조했슴..ㅠ
# 마감일 높은 기준으로 정렬 [6,5][4,60][4,40][4,10][3,30][2,50][1,20]
# 6일차부터 내려가면서 수행할 수 있는 과제의 최대값을 진행 = 거꾸로 내려가는 방식

# 6일차 - 유일하게 할 수 있는 [6,5] 진행
# 5일차 - 진행할 수 있는 과제가 없음
# 4일차 - [4,60][4,40][4,10] 중 최대값인 [4,60] 진행
# 3일차 - [4,40][4,10][3,30] 중 최대값인 [4,40] 진행
# 2일차 - [4,10][3,30][2,50] 중 최대값인 [2,50] 진행
# 1일차 - [4,10][3,30][1,20] 중 최대값인 [3,30] 진행

# filter(lambda x:x[0]>=i,case)를 이용하여 n일차일 때 n일차보다 과제마감일이 같거나 큰 것을 필터링함
import sys

N=int(sys.stdin.readline())

case=[]

for i in range(N):
    case.append(list(map(int, sys.stdin.readline().split())))

case.sort(reverse=True) # 마감일 순으로 정렬

day=max(case, key=lambda x:x[0])[0] # case 과제 마감일의 최대값을 day에 할당
sub=[]
total=[]

for i in range(day,0,-1):
    for k in filter(lambda x:x[0]>=i,case): # n일차보다 과제마감일이 같거나 큰 것들을 필터링하여 sub에 넣음
        sub.append(k)
    try:
        total.append(max(sub, key=lambda x:x[1])[1]) # sub에서 점수가 제일 높은 것을 total에 넣어줌
        case[case.index(max(sub, key=lambda x:x[1]))]=[0,0] # total에 할당된 값을 [0,0]으로 바꿔서 인덱스 값을 유지시킴
    except ValueError: # 5일차에 진행할 수 있는 과제가 없는 거처럼 sub에 값이 없어 ValueError가 발생하면 pass
        pass
    sub=[]

print(sum(total))

#-------------------------------------------------------------------------------------------------

# 오늘 날짜 day를 설정
# n일차 점수 최대값 - 전체의 최대값
# n일차 점수 최대값 > 전체의 최대값이라면 n일차 점수 최대값을 넣음
# n일차 점수 최대값 < 전체의 최대값이라면 전체의 최대값을 넣음
# 반복문을 돌리면서 day 증가
# 풀이 자체가 틀리..ㅁ...

import sys

N=int(sys.stdin.readline())

case=[]
total=[]

for i in range(N):
    case.append(list(map(int, sys.stdin.readline().split())))

case.sort() # [1,20][2,50][3,30][4,10][4,40][4,60][6,5]

EachDay=[[0,0]]

day=1

while True:
    for i in filter(lambda x: x[0]==day, case):
        EachDay.append(i)
        case.remove(i)

    EachDayM=max(EachDay, key=lambda x:x[1])
    TotalM=max(case, key=lambda x:x[1])

    if EachDayM[1] >= TotalM[1]:
        total.append(EachDayM[1])
    else:
        total.append(TotalM[1])
        case.remove(TotalM)

    if len(case)==0:
        break

    EachDay=[[0,0]]
    day+=1 
    # 30 50 40 60 5

#-------------------------------------------------------------------------------------------------

# 과제 마감일 기준으로 정렬
# 1. 과제 마감일 최솟값의 점수 > 과제 마감일 다음 최솟값의 점수 == 과제 마감일 최솟값 점수 할당
# 2. 과제 마감일 최솟값의 점수 < 과제 마감일 다음 최솟값의 점수 == 과제 마감일 다음 최솟값 점수를 할당
# 반복문의 반복횟수 == 날짜
# 위의 1,2번 중 하나를 하면 하루에 할 수 있는 과제를 완료한 것이기에 반복문의 반복 횟수 == 과제마감일이라면 삭제
# 과제 마감일 중 마지막 날짜를 M에 할당하고
# 반복문의 반복횟수 <= M 이라면 과제점수를 할당하고 break
# 반례 3, 1 1, 1 2, 1 3
import sys

N=int(sys.stdin.readline())

case=[]
total=[]
for i in range(N):
    case.append(list(map(int,sys.stdin.readline().split())))

case.sort() # [1,20][2,50][3,30][4,10][4,40][4,60][6,5]
M=max(case)[0] # 6

for i in range(1,N+1):
    try:
        if case[0][1] < case[1][1]: 
            total.append(case[1][1])
            case.remove(case[1])
        elif case[0][1] >= case[1][1]:
            total.append(case[0][1])
            case.remove(case[0])
        
        if case[0][0]==i:
            case.remove(case[0])
    except IndexError:
        if M >= i:
            total.append(case[0][1])
            break

print(sum(total))