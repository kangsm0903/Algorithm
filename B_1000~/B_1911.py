# now - 현재 좌표값을 설정하고 좌표값과 겹치거나 겹치지않는 것을 기준으로 작성했음
import sys

N,L=map(int,sys.stdin.readline().split()) # N 웅덩이 개수, L 널판지 길이
# 1<=N<=10,000 L은 양의 정수
length=[]

for i in range(N):
    length.append(list(map(int,sys.stdin.readline().split()))) # [[1,6],[13,17],[8,12]]

length.sort() # [1,6][8,12][13,17]

count=0
now=length[0][0]

def basic(a):
    global count,now
    if (length[i][1]-length[i][0])%L>0: # 나머지가 있으면
        count=count+(length[i][1]-length[i][0])//L+1 # 몫+1
        now=now+(((length[i][1]-length[i][0])//L+1)*L) 
    else:
        count=count+(length[i][1]-length[i][0])//L # 몫
        now=length[i][1]

for i in range(0,N):
    if now >= length[i][0]: # 좌표가 겹칠 때
        length[i][0]=now
        basic(i)
    else: # now < length[i][0] 안겹칠 떄
        now=length[i][0]
        basic(i)

print(count)