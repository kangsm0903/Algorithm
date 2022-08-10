# 문제를 이해하는데 시간이 걸린 문제, 그 외에는 2630,1780 풀이 방식과 똑같음
N=int(input())

graph=[list(map(int,input())) for _ in range(N)]

result=''

def recursive(row,column,n):
    global result
    base=graph[row][column]

    for i in range(row,row+n):
        for j in range(column,column+n):
            if graph[i][j]!=base:
                result+='('
                recursive(row,column,n//2) # 1
                recursive(row,column+n//2,n//2) # 2
                recursive(row+n//2,column,n//2) # 3
                recursive(row+n//2,column+n//2,n//2) # 4
                result+=')'
                return
    if base==0:
        result+='0'
    elif base==1:
        result+='1'


recursive(0,0,N)

print(result)

# -------------------------------------------------------------------------

N=int(input())

graph=[list(map(int,input())) for _ in range(N)]

result=''

def recursive(row,column,n):
    global result
    base=graph[row][column]

    for i in range(row,row+n):
        for j in range(column,column+n):
            if graph[i][j]!=base:
                result+='('
                for k in range(2):
                    for l in range(2):
                        recursive(row+(k*n//2),column+(l*n//2),n//2)
                result+=')'
                return
    if base==0:
        result+='0'
    elif base==1:
        result+='1'


recursive(0,0,N)

print(result)