# 3의 배수판정법으로 각 자릿수의 합이 3의 배수가 되야함
# 문제는 3의 배수가 아니라 30의 배수이기에 리스트에 0이라는 값이 하나라도 존재하면 30의 배수가 됨

import sys

N=list(map(int,sys.stdin.readline().rstrip('\n'))) # [2,1,0]

if sum(N)%3==0 and 0 in N: # 자릿수의 합이 3의 배수, 리스트에 0이 존재하는지
    N.sort(reverse=True)
    for i in N:
        print(i, end='')
else:
    print(-1)

