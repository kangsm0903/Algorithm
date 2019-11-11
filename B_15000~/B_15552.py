# 11/11
# 15552번
# python으로는 느려서 시간초과가 뜬다. 따라서 Rpython의 부분집합인 pypy를 사용했다.

T = input()
T = int(T)

a = []
b = []

for i in range(1,T+1):
    a.append(list(map(int, input().split())))
    b.append(sum(a[i-1]))

for i in range(1, T+1):
    print(b[i-1])