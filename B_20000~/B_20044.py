N=int(input())
W=sorted(list(map(int,input().split()))) # [1,7,5,8]

remain=[]

count=2*N-1
for i in range(N):
    remain.append(W[i]+W[count])
    count-=1

print(min(remain))