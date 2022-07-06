# re
N=int(input())

case=list(map(int,input().split())) # [6,9,5,7,4]
 
stack=[] # 최댓값을 저장할 스택
answer=[]# 수신 탑 인덱스를 저장

for i in range(N):
    while stack:
        if stack[-1][1] > case[i]: # 수신 가능한 상태
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i,case[i]])

print(" ".join(map(str,answer)))