N=int(input())

graph=[list(map(int,input().split())) for _ in range(N)]

minus=0
zero=0
one=0

def recursive(row, column,n):
    global minus, zero, one
    base=graph[row][column] # [0][0]


    for i in range(row,row+n):
        for j in range(column, column+n):
            if graph[i][j]!=base:
                recursive(row,column,n//3) # (0,0,3) 1사분면

                recursive(row,column+n//3,n//3) # (0,3,3) 2사분면

                recursive(row,column+n//3+n//3,n//3) # (0,6,3) 3사분면

                recursive(row+n//3,column,n//3) # (3,0,3) 4사분면

                recursive(row+n//3,column+n//3,n//3) # (3,3,3) 5사분면

                recursive(row+n//3,column+n//3+n//3,n//3) # 6사분면

                recursive(row+n//3+n//3,column,n//3) # 7사분면 (6,0,3)

                recursive(row+n//3+n//3,column+n//3,n//3) # 8사분면

                recursive(row+n//3+n//3,column+n//3+n//3,n//3) # 9사분면
                return

    if base==-1:
        minus+=1
        return
    elif base==0:
        zero+=1
        return
    elif base==1:
        one+=1
        return

recursive(0,0,N)
# 876543210

print(minus)
print(zero)
print(one)