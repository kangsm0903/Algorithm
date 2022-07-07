N=int(input())

case=list(map(int,input().split())) # [6,9,5,7,4]
 
stack=[] # 최댓값을 저장할 스택
answer=[]# 수신 탑 인덱스를 저장

for i in range(N):
    while stack: # [[1,9]]
        if stack[-1][1] > case[i]: # stack의 top의 높이 > case[i] i 인덱스 번호의 높이
            answer.append(stack[-1][0]+1) # stack top의 idx+1 삽입
            break
        else:
            stack.pop()
    if not stack: # 스택이 비어있으면 0 삽입
        answer.append(0)
    stack.append([i,case[i]])

print(" ".join(map(str,answer)))