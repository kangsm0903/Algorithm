# 같은 수 여러 번 골라도 됨 - visited 필요없음
# set함수를 이용해서 중복된 것들을 걸러내야함
# 비내림차순

N,M=map(int,input().split()) # 4 2
 
case=list(map(int,input().split())) # 9 7 9 1
case.sort()

result=[]
test=set()

def is_promising():
    base=result[0]
    for i in range(1,len(result)):
        if base>result[i]:
            return False
        else:
            base=result[i]
            continue
    return True

def BruteForce():
    global result
    if len(result)==M: 
        test.add(tuple(result))
        return

    for i in range(len(case)):
        result.append(case[i])
        if is_promising():
            BruteForce()
        result.pop()

BruteForce()

test=list(test)
test.sort()

for i in test:
    print(*i)

