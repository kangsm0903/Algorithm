# 조합 combinations를 이용한 풀이
from itertools import combinations

N,S=map(int,input().split()) # n개의 정수, 더해서 S가 되는 값

case=list(map(int,input().split()))

result=[]
cnt=0

for i in range(1,len(case)+1):
    result=combinations(case,i)

    for i in result:
        if sum(i)==S:
            cnt+=1

print(cnt)

# ----------------------------------------------------------
# 재귀, 백트래킹을 이용한 풀이

# depth 0 :                    {공집합}
# depth 1 :          {공집합}               {-2}
# depth 2 :     {공집합}   {3}       {-2}         {-2,3}
# depth 3 : {공집합} {5} {3} {3,5} {-2} {-2,5} {-2,3} {-2,3,5}

# 46번 = left 집합을 추가하지않는 경우
# 47번 = right 집합을 추가하는 경우

N,S=map(int,input().split()) # n개의 정수, 더해서 S가 되는 값
case=list(map(int,input().split())) # -2 5 3
cnt=0

def BackTrack(idx, subsum):
    global cnt

    if idx>=N: # N이 최대깊이에 도달하면 return
        return

    subsum+=case[idx]

    if subsum==S:
        cnt+=1

    BackTrack(idx+1,subsum-case[idx]) # left_node = 추가하지 않는 경우
    BackTrack(idx+1,subsum) # right_node = 추가하는 경우
    

BackTrack(0,0)
print(cnt)
