# [100,99,10]과 같이 모든 로프를 쓰지 않는 경우도 고려하는게 포인트였음
import sys

N=int(sys.stdin.readline())

rope=[]

for i in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True) # [100,99,10]

result=rope[0]

for i in range(1,N):
    if rope[i]*(i+1) > result:
        result=rope[i]*(i+1)
    else:
        pass

print(result)