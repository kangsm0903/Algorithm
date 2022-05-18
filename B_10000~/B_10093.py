# A==B 일수도 있었다는 점 - if문을 따로 추가
# A < B 가 아니라 A > B 일수도 있었다는 점 - abs() 및 min, max로 해결

import sys

A,B=map(int,sys.stdin.readline().split())

if A==B:
    count=0
else:
    count=abs(A-B)-1

print(count)

for i in range(min(A,B)+1,max(A,B)):
    print(i, end=' ')