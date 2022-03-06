# 기지국의 개수가 2개면 센서 사이의 거리가 가장 큰 한 개의 장소 기준으로 2개 세우면 됨
# 기지국의 개수가 3개면 센서 사이의 거리가 가장 큰 두 개의 장소 기준으로 3개 세우면 됨
# 위와 같이하면 센서 사이의 거리가 큰 곳은 카운트 되지않기에 나머지를 더하면 최소합
N=int(input()) # 센서 개수

K=int(input()) # 기지국 개수

if K>=N:
    print(0)
else:
    case=list(map(int,input().split())) # [1,6,9,3,6,7]
    case.sort() # 오름차순 정렬 [1,3,6,6,7,9]

    case1=[] # [2,3,0,1,2]

    for i in range(len(case)-1): # 0~5
        case1.append(case[i+1]-case[i])

    case1.sort(reverse=True)

    for i in range(K-1): 
        case1.remove(case1[0])

    print(sum(case1))