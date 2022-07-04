N=int(input()) # n개의 숫자 = 8개

mainStack=[]
resultStack=[]

for i in range(N):
    mainStack.append(int(input())) # [4,3,6,8,7,5,2,1]

first=0

case=[]

for i in range(N): # 0~7
    if first<mainStack[i]:
        for k in range(first,mainStack[i]):
            resultStack.append(k+1)
            case.append('+')
        first=mainStack[i]
    if resultStack[-1]==mainStack[i]:
        resultStack.pop()
        case.append('-')
    else:
        case=['NO']
        break

for i in range(len(case)):
    print(case[i])

# -----------------------------------------------

n=int(input()) # 8

number_sequence=[i for i in range(n,0,-1)] # [8,7,6,5,4,3,2,1]
# number_sequence에서 내림차순으로 한 이유는 47번 줄 list.pop()을 사용하기 위해서임
making_sequence=list()                     # [4,3,6,8,7,5,2,1]

for _ in range(n): # [4,3,6,8,7,5,2,1]
    making_sequence.append(int(input()))

stack=list()
result=list()
can_make=True

for i in range(n):
    while len(number_sequence)!=0 and number_sequence[-1]<=making_sequence[i]:
        # number_sequence의 길이가 0이 아니면서 마지막 원소 <= making_sequence[i] 이여야 한다.
        stack.append(number_sequence.pop())
        result.append('+')
    
    if stack[-1]== making_sequence[i]:
        stack.pop()
        result.append('-')
    else:
        can_make=False
        break

if can_make:
    for i in result:
        print(i)
else:
    print('NO')