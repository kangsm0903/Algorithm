import sys

A,B,C=map(int,sys.stdin.readline().split())

def eng(a,b):
    if b==1:
        return a%C
    else:
        temp=eng(a,b//2)
        if b%2==0:
            return temp*temp%C
        else:
            return temp*temp*a%C

a=eng(A,B)
print(a)