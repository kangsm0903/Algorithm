N=int(input())

case=list(map(int,input().split()))

case.remove(max(case))

print(sum(case))