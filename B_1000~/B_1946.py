import sys

T=int(sys.stdin.readline())

result=[]

for i in range(T):
    case=[]
    count=1
    N=int(sys.stdin.readline())
    for k in range(N):
        case.append(list(map(int,sys.stdin.readline().split())))
    
    case.sort() # 오름차순으로 정렬 [1,4][2,3][3,2][4,1][5,5]
                # 오름차순 - 서류심사 기준으로 정렬하였기에 앞에서부터 면접시험에서 뒤떨어지는 사람을 없애면 됨
    minimum=case[0][1] # 서류심사 1등의 면접시험

    for l in range(1,N):         # case[l][1]>minimum이라면 -> [1,4][2,5]인 경우이기에 [2,5]는 탈락임
        if case[l][1] < minimum: # case[l][1]<minimum이라면 -> [1,4][4,2]인 경우이기에 [4,2]는 합격임
            minimum=case[l][1]   # 최소를 case[l][1]로 갱신해줌
            count+=1

    result.append(count)

for m in result:
    print(m)

# ---------------------------------------------------------------------------------------------------------------

import sys

T=int(sys.stdin.readline()) # 1<=T<=20

result=[]

for i in range(T):
    N=int(sys.stdin.readline()) # 1<=N<=100000
    case=[]
    for k in range(N):
        case.append(list(map(int,sys.stdin.readline().split())))
    case.sort(key=lambda x:x[0]+x[1], reverse=True) # x[0]+x[1]의 값이 큰 것부터 내림차순으로 정렬

    case1=case.copy()

    # 20 * 100,000 * 100,000 여기서 시간초과 터짐
    for l in case1:
        for m in filter(lambda x:x[0]>l[0] and x[1]>l[1],case): # 필터함수로 x[1],x[0]보다 큰 것들을 걸러냄
            case.remove(m)

    result.append(len(case))

for i in range(T):
    print(result[i])