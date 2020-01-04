fix, chan, pri = list(map(int, input().split()))

if chan>=pri:
    print(-1)
else:
    print(int(fix/(pri-chan)+1))

# 손익분기점이 -1이 되는 조건을 찾는 것이 관건인 문제
# count를 구하는 것도 변수를 두는게 아닌 변수를 도출하게 식을 쓰는 것이 핵심이라 봄