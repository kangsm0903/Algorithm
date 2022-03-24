import sys

N, M=map(int,sys.stdin.readline().split()) # 2<=N<=100, 1<=M<=N

case=list(map(int,sys.stdin.readline().split())) # 이용하는 버스들

busCase=[]

count=0

for i in range(N):
    busCase.append(list(map(int,sys.stdin.readline().split())))

for i in range(M-1):
    count+=busCase[case[i]-1][case[i+1]-1]

print(count)