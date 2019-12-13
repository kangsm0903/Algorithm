# 12/14 2908번
# reversed() 순서가 뒤바뀐 배열을 반환

N = list(map(int, input().split()))

A = list(reversed(list(str(N[0]))))
B = list(reversed(list(str(N[1]))))

A = ''.join(A)
B = ''.join(B)

if A>B:
    print(A)
else:
    print(B)