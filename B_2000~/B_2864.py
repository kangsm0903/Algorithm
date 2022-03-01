import sys

A,B=map(str,sys.stdin.readline().split()) # 단어의 개수 1<=N<=10

a=list(A) # [1,1]
b=list(B) # [2,5]

def mn(a,b):
    global m
    for i in a:
        if i=='6':
            a[a.index(i)]='5'
    for i in b:
        if i=='6':
            b[b.index(i)]='5'
    m=int("".join(a))+int("".join(b))
        

def mx(a,b):
    global M
    for i in a:
        if i=='5':
            a[a.index(i)]='6'
    for i in b:
        if i=='5':
            b[b.index(i)]='6'
    M=int("".join(a))+int("".join(b))

mn(a,b)
mx(a,b)

print(m,M)