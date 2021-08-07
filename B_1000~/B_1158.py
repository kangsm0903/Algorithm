# 요세푸스 문제

N = list(map(int, input().split()))

A = []
B = []
C = []
number = N[1]-1
count = N[1]

for i in range(1,N[0]+1):
    A.append(i)


while len(B) != N[0]: # 같아지면 끝
    while number >= len(A):
        base = len(A)
        for i in C:
            A.remove(i)
        C = []
        number = number - base
    B.append(A[number])
    C.append(A[number])
    number = number + count

B = [str(i) for i in B]
print("<"+(','.join(B)).replace(",",", ")+">")

# B = ','.join(B)
# B = B.replace(",",", ")
# print("<"+B+">")