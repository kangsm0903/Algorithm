# 과제 마감일 기준으로 정렬
# 1. 과제 마감일 최솟값의 점수 > 과제 마감일 다음 최솟값의 점수 == 과제 마감일 최솟값 점수 할당
# 2. 과제 마감일 최솟값의 점수 < 과제 마감일 다음 최솟값의 점수 == 과제 마감일 다음 최솟값 점수를 할당
# 반복문의 반복횟수 == 날짜
# 위의 1,2번 중 하나를 하면 하루에 할 수 있는 과제를 완료한 것이기에 반복문의 반복 횟수 == 과제마감일이라면 삭제
# 과제 마감일 중 마지막 날짜를 M에 할당하고
# 반복문의 반복횟수 <= M 이라면 과제점수를 할당하고 break
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