# 10869번

a = list(input().split())

# a = list(map(int,a))

for A in a[0]:
    for B in a[1]:
        print(int(A) + int(B))
        print(int(A) - int(B))
        print(int(A) * int(B))
        print(int(A) // int(B))
        print(int(A) % int(B))

a, b = input().split()

a = int(a)
b = int(b)

print(a+b, a-b, a*b, a//b, a%b)