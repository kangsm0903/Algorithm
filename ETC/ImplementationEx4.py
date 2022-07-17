# 문자열이 입력되었을 때 문자를 하나씩 확인한다.
# 숫자인 경우 따로 합계를 계산
# 알파벳인 경우 별도의 리스트에 저장

A=list(input()) # 문자열 길이 <= 10,000

A.sort(reverse=True)

num=[i for i in range(10)] # [0,1,2,3,4,5,6,7,8,9]

case=[]

for i in A:
    try:
        int(A[-1])
        case.append(int(A.pop()))
    except ValueError:
        A.sort()
        A.append(str(sum(case)))
        break

print(''.join(A))

# -------------------------------------------------------------
# isalpha() 이게 포인트였음

data=input()
result=[]
value=0

# 문자를 하나씩 확인
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value+=int(x)
    
result.sort()

if value!=0: # value가 0이 아니면 result에 append
    result.append(value)

print(''.join(result))