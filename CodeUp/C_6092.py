a=int(input())
b=list(map(int, input().split( )))

for i in range(1,24):
    print(b.count(i), end=" ")