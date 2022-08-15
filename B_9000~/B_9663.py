# 퀸은 한 행에 하나씩 밖에 못 두기에 idx를 row로 value를 column으로 설정
# [1,3,0,2] == [0,1] [1,3] [2,0] [3,2] 
# 만약 [1,1,0,2] == [0,1] [1,1] [2,0] [3,2] 으로 첫번째 두번째 퀸의 위치가 겹치는 것을 볼 수 있음
# 따라서 row[x]==row[i]이면 False 반환 (다른 행 같은 열에 퀸이 놓여진 상황)

# (3,3) 기준 킹각선 = (2,2)(1,1)(0,0) => (3,3)-킹각선 = (1,1) (2,2) (3,3)
# (3,3) 기준 킹각선 = (2,4)(1,5)(0,6) => (3,3)-킹각선 = (1,-1)(2,-2)(3,-3)
# [(3,3)-킹각선][1] == row[x]-row[i]
# [(3,3)-킹각선][0] == x-i

n=int(input())

ans=0
row=[0]*n

def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
        
    return True

def n_queens(x): # row
    global ans
    if x==n:
        ans+=1
        return

    else:
        for i in range(n): # column
            row[x]=i # (x,i)
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)

# ---------------------------------------------------------------------------------

# N*N의 체스판에서 N개의 퀸을 서로 공격할 수 없는 위치에 놓을 수 있는 경우의 수
N=int(input())

Queen_location=[]

cnt=0

def BackTrack(row):
    global cnt
    if row==N:
        cnt+=1
        Queen_location.pop()
        return

    for i in range(N): # column 하나씩 넣어볼거임
        basic=0
        if len(Queen_location)==0:
            Queen_location.append((row,i)) # (row,column)
            BackTrack(row+1)
        else:
            for j in Queen_location:
                if j[1]==i or sum(j)==row+i or j[0]-j[1]==row-i:
                    basic=-1
            if basic==0: # y축, 대각선 둘 다 겹치는 부분이 없다면
                Queen_location.append((row,i))
                BackTrack(row+1)
    try:
        Queen_location.pop()
    except IndexError:
        return
    
BackTrack(0)

print(cnt)