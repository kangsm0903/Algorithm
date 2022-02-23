# 종료시간을 기준으로 정렬한 후 시작시간이 종료시간보다 크거나 같으면 추가하는 과정
import sys

N=int(sys.stdin.readline())

lofi=[]
count=1
for i in range(N):
    lofi.append(list(map(int,sys.stdin.readline().split())))
    # lofi.sort(key=lambda x:x[0]) for문 안에 정렬을 넣었기에 계속 시간초과로 실패했었던 거임
    # lofi.sort(key=lambda x:x[1])

lofi.sort(key=lambda x:x[0]) # 시작시간으로 정령
lofi.sort(key=lambda x:x[1]) # 끝나는 시간으로 정렬

static=lofi[0][1]

for k in range(1,N): # 0~10
    if static<=lofi[k][0]:
        static=lofi[k][1]
        count+=1

print(count)

# ----------------------------------------------------------------------------------------------------
# 시간초과 풀이 - 오래 전이라 어떤 생각으로 풀이했는지 기억 안남
N = int(input())

X=[]
Y=[]
Sli=[] # 차이 = 간격


for i in range(N):
    x,y=input().split()
    X.append(int(x))
    Y.append(int(y))
    Sli.append(Y[i]-X[i])

z = Y.index(min(Y)) # 0
count=1
while True:
    for i in range(N):
        if z > X[i]:
            Sli.remove(Sli[i])
        
    a = Sli.index(min(Sli))