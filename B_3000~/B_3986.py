# "AA","BB"를 없애는 방식으로 접근했음
# 하나씩 stack에 넣어주고 join으로 합쳤을 때 "BB","AA"가 존재한다면 pop()으로 맨 뒤의 2개의 원소를 추출
# 이렇게 반복 후 stack에 남은 원소가 없다면 count+=1

N=int(input())

count=0

for i in range(N):
    stack=[]
    target=list(input()) # [A,B,A,B]
    stack.append(target.pop()) # target=[A,B,A] / stack=[B]
    for k in range(len(target)):
        stack.append(target.pop()) # target=[A,B] / stack[B,A]
        # "BB", "AA"가 존재하면 맨 뒤의 원소 2개를 추출
        if "BB" in ''.join(stack):
            stack.pop()
            stack.pop()            
        elif "AA" in ''.join(stack):
            stack.pop()
            stack.pop()
        else:
            pass
    # stack의 원소가 없다면 count+=1
    if len(stack)==0:
        count+=1
    else:
        pass

print(count)

# --------------------------------------------------------------------------------------
# 좀 더 빠르고 간결한 풀이

n=int(input())

count=0

for _ in range(n):
    words=list(input())
    stack=[]
    for i in range(len(words)): # 0~5
        if len(stack)==0:
            stack.append(words[i])
        elif stack[-1]==words[i]:
            stack.pop()
        elif stack[-1]!=words[i]:
            stack.append(words[i])
    if len(stack)==0:
        count+=1
    else:
        pass
print(count)