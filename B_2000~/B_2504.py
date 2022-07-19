case=list(input())

stack=[]

result=0
test=1

for i in range(len(case)):
    if case[i]=='(': # 열린 괄호는 바로바로 넣어줌
        stack.append(case[i]) 
        test*=2
    elif case[i]=='[':
        stack.append(case[i])
        test*=3

    elif case[i]==')': # 닫힌 괄호일 때
        if not stack or stack[-1]=='[':
            result=0
            break
        elif case[i-1]=='(':
            result+=test
            test//=2
            stack.pop()
        else:
            test//=2
            stack.pop()
        
    elif case[i]==']':
        if not stack or stack[-1]=='(':
            result=0
            break
        elif case[i-1]=='[':
            result+=test
            test//=3
            stack.pop()
        else:
            test//=3
            stack.pop()
    
if stack:
    print(0)
else:
    print(result)

# ---------------------------------------------------------------

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