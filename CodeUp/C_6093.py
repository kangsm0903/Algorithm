a = int(input())
b = list(map(int, input().split( )))
b.reverse()
for i in b:
    print(i, end=" ")