# 삼항연산 사용
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

min = a if a<b else b
min = min if min<c else c
print(min)