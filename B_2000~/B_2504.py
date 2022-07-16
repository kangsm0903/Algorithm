# reference

T=list(input())

stack=[]
result=0
tmp=1

for i in range(len(T)): # 열린 괄호는 그냥 넣어줌
    if T[i]=='(':
        stack.append(T[i])
        tmp*=2
    elif T[i]=='[':
        stack.append(T[i])
        tmp*=3

    elif T[i]==')': # 닫는 괄호
        if not stack or stack[-1]=='[':
            result=0
            break
        elif T[i-1]=='(':
            result+=tmp
        stack.pop()
        tmp//=2

    else:
        if not stack or stack[-1]=='(':
            result=0
            break
        elif T[i-1]=='[':
            result+=tmp
        stack.pop()
        tmp//=3

if stack:
    print(0)
else:
    print(result)