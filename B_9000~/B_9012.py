# 3986번 빠른 풀이와 매우 유사한 방식
# 다른 점으로는 '('와 ')' 짝꿍이여야하는데 ')'와'(' 도 짝꿍으로 포함되는 경우가 핵심이였음
# 따라서 16번줄에서 case[k], stack[-1]을 각각 따로 설정해줬음
# 어짜피 case[k]==')'이여야하고 stack[-1]=='('여야하기 때문이다 -- 헷갈리면 잘 생각해보면 됨

T=int(input())

count=0

for i in range(T):
    case=list(input())
    stack=[]

    for k in range(len(case)):
        if len(stack)==0:
            stack.append(case[k])
        elif case[k]==')' and stack[-1]=='(':
            stack.pop()
        elif case[k]==stack[-1]:
            stack.append(case[k])
    
    if len(stack)==0:
        print('YES')
    else:
        print('NO')
