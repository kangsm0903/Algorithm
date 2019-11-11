# 11/11 빼빼로데이
# 10950

T = input()

T = int(T)

a = []
b = []

for i in range(1,T+1):
    a.append(list(map(int, input().split())))
    b.append(sum(a[i-1]))

for i in range(1,T+1):
    print(b[i-1])