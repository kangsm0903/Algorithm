a=int(input())

case=list(map(int,input().split()))

target=int(input())

if target not in case:
    print(0)
else:
    print(case.count(target))

# ---------------------------------------------------
# 단순히 입력받고 count로 바로 target 찾아도 됨
# 굳이 case에 target이 있는지 확인을 안해도 됨
a=int(input())

case=list(map(int,input().split()))

target=int(input())

print(case.count(target)) 
