import sys

A,B=map(int, sys.stdin.readline().split())

cnt=0

while A!=B: # A와B가 같으면 멈춤
    C=B%10 # 마지막 자릿수 값
    if B%10!=1 and B%2==1: # 홀수이면서 마지막 자릿수가 1이 아닌 수는 계산 불가능하기에 -2
        cnt=-2
        break
    elif C==1:# 마지막 자릿수가 1이면 몫으로 바꿔줌
        B=B//10
    elif A>B: # 계속 계산을 진행하다가 A>B가 되면 더이상 가능한 연산이 없기에 -2
        cnt=-2
        break
    else: # 나머지는 2를 나누는 연산을 진행
        B=B//2
    cnt+=1

print(cnt+1)