# 색종이 길이가 6이면 바로 판 추가
# 색종이 길이가 5이면 판 추가 후 1-11개 남음
# 색종이 길이가 4이면 2, 1만 가능
# 색종이 길이가 3이면 3,2,1 가능
import sys

case=[]

for i in range(6):
    case.append(int(sys.stdin.readline()))

case.reverse() # 뒤집기 0 1 1 0 3 5
cnt=6
total=0

one=0
two=0
three=0

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
            two+=4  # 2-4개 추가
            one+=11 # 1-11개 추가
        elif i%4==2:# 나머지가 2일 때 판 하나를 추가하고
            total+=1
            two+=3  # 2-3개 추가
            one+=6  # 1-6개 추가
        elif i%4==3:# 나머지가 3일 때 판 하나를 추가하고
            total+=1
            two+=1  # 2-1개 추가
            one+=3  # 1-3개 추가
    elif  cnt==2 and i-two>0: # 2이며 i가 기존 two보다 클 때
        total+=(i-two)//9 # i에서 two를 뺀 것들 중 9로 나누었을 때 몫만큼 판 추가
        if (i-two)%9>0:   # 나머지가 있을 경우
            total+=1      # 판 추가
            one+=(36-4*(i-two)%9) # 남은 two를 one으로 바꿔준다.
    elif cnt==2 and two-i>=0: # 2이며 i가 기존 two보다 작을 때
        two-=i # two에서 i를 빼고 남은 two를 one으로 바꿔준다.
        one+=two*4

    elif cnt==1 and i-one>0: # 1이며 i가 기존 one보다 클 때
        total+=(i-one)//36   # i-one을 36으로 나누었을 때 몫만큼 판 추가
        if (i-one)%36>0:     # 나머지가 있으면 판 추가
            total+=1
    elif cnt==1 and one-i>=0:# 1이며 i가 기존 one보다 작을 때
        one-=i # one에서 i를 빼줌

    cnt-=1
    
print(total)