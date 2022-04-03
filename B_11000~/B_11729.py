# 하노이의 탑 재귀함수
# 1. 작은 원반 n-1개를 A->B로 이동
# 2. 큰 원반(맨 아래)를 A->C로 이동
# 3. 작은 원반 n-1개를 B->C로 이동
# 
case=[]

def HanoiTower(num,A, B, C):
    global cnt
    global case
    if num==1: # 움직일 원반이 하나일 때 
        cnt+=1
        case.append(int(A))
        case.append(int(C))
    else:
        HanoiTower(num-1,A,C,B) # 작은 원반 n-1개를 A->C->B로 이동
        case.append(int(A))     # 큰 원반 1개를 A->C로 이동
        case.append(int(C))     
        cnt+=1
        HanoiTower(num-1,B,A,C);# 작은 원반 n-1개를 B->A->C로 이동

N=int(input())
cnt=0

HanoiTower(N,'1','2','3')

print(cnt)
for i in range(0,cnt*2,2):
    for k in case[i:i+2]:
        print(k, end=' ')
    print()