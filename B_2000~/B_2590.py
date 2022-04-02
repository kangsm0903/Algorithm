# 색종이 6칸이 i개라면 판 i개 추가
# 색종이 5칸이 i개라면 판 i개 추가 - 1칸짜리 11*i만큼 추가
# 색종이 4칸이 i개라면 판 i개 추가 - 2칸짜리 5*i만큼 추가

# 색종이 3칸이 i개라면 판 i개 추가 
# - i%4가 1일 때, 2칸짜리 5개 추가, 1칸짜리 7개 추가
# - i%4가 2일 때, 2칸짜리 3개 추가, 1칸짜리 6개 추가
# - i%4가 3일 때, 2칸짜리 1개 추가, 1칸짜리 5개 추가

# 색종이 2칸이 i개일 때, 2칸 쌓여있는 것 == two라 한다면,
# two>=i 일 때, (two-i) 남은 2칸짜리를 1칸으로 바꿔줌 == (two-i)*4
# two<i  일 때, (i-two)//9 몫만큼 판 추가, 나머지가 존재하면 판 1개 추가 (9-(i-two)%9)*4 판 추가 후 남은 부분을 1칸으로 변환

# 색종이 1칸이 i개 일때, 1칸 쌓여있는 것 == one이라 한다면,
# one>=i 일 때, 쌓여있는 것에 다 넣으면 되니 판 추가 할 일 없음
# one<i  일 때, (i-one)36 몫만큼 판 추가, 나머지가 존재하면 판 1개 추가 후 total 반환

# 생각해야할 조건들이 많았음

import sys

case=[]

for i in range(6):
    case.append(int(sys.stdin.readline()))

case.reverse() # 뒤집기 0 1 1 0 3 5
cnt=6
total=0

one=0
two=0

for i in case:
    if cnt==6 and i>0: # 6 그냥 판 추가
        total+=i
    elif cnt==5 and i>0: # 5 - 1-11개 추가 
        one+=11*i
        total+=i
    elif cnt==4 and i>0: # 4 - 2-5개 추가
        two+=5*i
        total+=i
    elif cnt==3 and i>0: # 3
        total+=i//4 # 일단 몫만큼 판 추가
        if i%4==1:  # 나머지가 1일 때 판 하나를 추가하고
            total+=1
            two+=5  # 2-5개 추가
            one+=7 # 1-7개 추가
        elif i%4==2:# 나머지가 2일 때 판 하나를 추가하고
            total+=1
            two+=3  # 2-3개 추가
            one+=6  # 1-6개 추가
        elif i%4==3:# 나머지가 3일 때 판 하나를 추가하고
            total+=1
            two+=1  # 2-1개 추가
            one+=5  # 1-5개 추가
    elif cnt==2:
        if two>=i:
            one+=(two-i)*4
            pass # 단순히 지금까지 쌓인 것들에 색종이 2칸짜리를 넣으면 됨
        else: # i>two    i-two == 남은 것들
            total+=(i-two)//9
            remind=(i-two)%9 # 나머지
            if remind>0:
                total+=1
                one+=(9-remind)*4
    elif cnt==1:
        if one>=i:
            pass # 지금까지 쌓인 1칸들에 색종이 1칸짜리를 넣으면 됨
        else: # i>one
            total+=(i-one)//36
            remind=(i-one)%36
            if remind>0:
                total+=1
    cnt-=1
    
print(total)