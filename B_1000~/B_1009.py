N = int(input())

M = [[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
L = []

for i in range(0,N):
    L.append(list(map(int,input().split())))

for k in range(0,len(L)):
    if L[k][0] >= 10:
        L[k][0] = L[k][0] % 10
    Remainder = int(L[k][1] % len(M[L[k][0]]))
    print(M[L[k][0]][Remainder-1])