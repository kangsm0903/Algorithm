import sys

N=int(sys.stdin.readline()) # 200

n=int((N*2)**(1/2)) 
# (n^2)/2 < n(n+1)/2 이므로 (n^2)/2을 기준으로 n값을 할당했음

def sigma(a): # sigma 1부터 k까지의 합
    return a*(a+1)/2

if sigma(n)>N: 
    n-=1 # sigma 20이라면 210으로 N보다 크기에 n을 하나 줄여준다.
# n이 19이면 1,2,3...,17,18,19으로 합이 190 인데 
# 마지막 숫자인 19만 200값에 맞게 29로 바꾸면 되기에 sigma의 K값만 반환해주면 된다.

print(n)