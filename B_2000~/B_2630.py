# 1780 풀이와 같음 

N=int(input())

graph=[list(map(int,input().split())) for _ in range(N)]

one_blue=0
zero_white=0

def recursive(row, column, n):
    global one_blue, zero_white
    base=graph[row][column]

    for i in range(row,row+n):
        for j in range(column,column+n):
            if graph[i][j]!=base:
                recursive(row,column,n//2) # 1사분면
                recursive(row+n//2,column,n//2) # 2사분면 
                recursive(row,column+n//2,n//2) # 3사분면
                recursive(row+n//2,column+n//2,n//2) # 4사분면
                return
    if base==0:
        zero_white+=1
    elif base==1:
        one_blue+=1
    
recursive(0,0,N)
print(zero_white)
print(one_blue)

# ---------------------------------------------------------------------

N=int(input())

graph=[list(map(int,input().split())) for _ in range(N)]

one_blue=0
zero_white=0

def recursive(row, column, n):
    global one_blue, zero_white
    base=graph[row][column]

    for i in range(row,row+n):
        for j in range(column,column+n):
            if graph[i][j]!=base:
                for k in range(2):
                    for l in range(2):
                        recursive(row+(k*n//2),column+(l*n//2),n//2)
                return
    if base==0:
        zero_white+=1
    elif base==1:
        one_blue+=1
    
recursive(0,0,N)
print(zero_white)
print(one_blue)