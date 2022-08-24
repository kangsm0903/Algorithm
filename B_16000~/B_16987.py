# 처음 나의 풀이와 다른 점이 나는 깨진 계란을 바로바로 체크했다면
# 이 풀이는 마지막에서야 깨진 계란들을 카운트해줬기에 나의 풀이보다 간결할 수 있었음

N=int(input()) # 계란 갯수

eggs=[list(map(int,input().split())) for _ in range(N)]

answer=0

def dfs(index,eggs):
    global answer
    if index==N: # 가장 오른쪽 계란을 골랐다면
        count=0
        for egg in eggs: # 내구도가 0이하인 것들을 count해줌
            if egg[0]<=0:
                count+=1
        answer=max(answer,count)
        return

    if eggs[index][0]<=0: # 선택한 계란이 깨져있다면 넘어감
        dfs(index+1,eggs)
    else:
        isAllBroken=True
        for i in range(N):
            if index!=i and eggs[i][0]>0: # 선택한 계란이 아니고, 때릴 계란의 체력이 0보다 크면
                isAllBroken=False
                eggs[index][0]-=eggs[i][1]
                eggs[i][0]-=eggs[index][1]

                dfs(index+1,eggs)

                eggs[index][0]+=eggs[i][1]
                eggs[i][0]+=eggs[index][1]
        if isAllBroken==True:
            dfs(N,eggs)

dfs(0,eggs)
print(answer)

# ---------------------------------------------------------------------------------------------
# 처음의 나의 풀이 - 시간초과
# broken으로 깨진 경우를 따로 체크하려고한 부분이 아쉬웠음
N=int(input()) # 계란 수

case=[list(map(int,input().split())) for _ in range(N)]

broken=[0]*N # 깨진 경우
result=set()

def dfs(egg_num):
    global result

    if egg_num==N:
        if broken.count(1)>2:
            result.add(broken.count(1))
        else:
            result.add(broken.count(1))
        return

    egg=case[egg_num]

    for i in range(len(case)):
        # 들고있는 계란이거나 아래에 깨진 계란이거나, 들고있는데 깨진 계란일 경우
        if i==egg_num or broken[i]==1 or broken[egg_num]==1: 
            continue
        
        if egg[0]<=case[i][1] and egg[1]>=case[i][0]: # 둘 다 깨지는 경우
            broken[egg_num]=1
            broken[i]=1

            dfs(egg_num+1)

            broken[egg_num]=0
            broken[i]=0
            
        elif egg[0]>case[i][1] and egg[1]>=case[i][0]: # case만 깨지는 경우
            broken[i]=1 # 깨짐
            egg[0]-=case[i][1]

            dfs(egg_num+1)

            broken[i]=0
            egg[0]+=case[i][1]

        elif egg[0]<=case[i][1] and egg[1]<case[i][0]: # egg만 깨지는 경우
            broken[egg_num]=1 # 깨짐
            case[i][0]-=egg[1]

            dfs(egg_num+1)

            broken[egg_num]=0
            case[i][0]+=egg[1]

        elif egg[0]>case[i][1] and egg[1]<case[i][0]: # 둘 다 안깨지는 경우
            egg[0]-=case[i][1]
            case[i][0]-=egg[1]

            dfs(egg_num+1)

            egg[0]+=case[i][1]
            case[i][0]+=egg[1]

    dfs(egg_num+1)

dfs(0)  

print(max(result))