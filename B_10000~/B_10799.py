T=list(input())

stack=[]

count=0

for i in range(len(T)):
    if T[i]=='(':
        stack.append(T[i])
    elif T[i]==')' and T[i-1]=='(': # razor
        stack.pop()
        count+=(len(stack))
        
    elif T[i]==')' and T[i-1]==')': # 쇠막대기 표현
        stack.pop()
        count+=1

print(count)