import sys
import math

case=[0,0,0,0,0,0,0,0,0,0] # 0,1,2,3,4,5,6,7,8,9

N=list(str(sys.stdin.readline().rstrip('\n'))) # max=1,000,000

for i in N:
    case[int(i)]+=1

if case.index(max(case))==6 or case.index(max(case))==9:
    sub=math.ceil((case[6]+case[9])/2)
    case[6]=0
    case[9]=0
    if sub>max(case):
        print(sub)
    else:
        print(max(case))
else:
    print(max(case))

# -----------------------------------------------------------

room_number=input()

room_check={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0} # dictionary 사용
# 9는 6에다가 +1을 해줌

for i in range(len(room_number)):
    if(room_number[i] in ['6','9']):
        room_check['6']+=1
    else:
        room_check[room_number[i]]+=1

room_check['6']=math.ceil(room_check['6']/2) # 6의 value는 2로 나누고 올림 해줌
print(max(room_check.values()))