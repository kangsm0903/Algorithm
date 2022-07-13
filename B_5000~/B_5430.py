# R = 뒤집기 D = 버리기
# 먼저 R의 개수를 counting함
# R의 개수가 짝수라면 deque의 맨 앞 원소를 pop
# R의 개수가 홀수라면 deque의 맨 뒤 원소를 pop
# 주어진 모든 함수를 실행했다면 R의 개수가 짝수이면 그대로
# R의 개수가 홀수이면 배열을 거꾸로 뒤집어서 출력해줌

from collections import deque

T=int(input()) # T<=100

for i in range(T):
    breaker=False
    p=list(input()) # 1<=p<=100,000 / RDD
    n=int(input()) # 0<=n<=100,000 / 4
    a=input().strip('[]').split(',')
    dequeue=deque(a) # [1,2,3,4]
    count=0
    for k in p:
        if k=='R':
            count+=1
        elif k=='D' and len(dequeue)>0 and a!=['']:
            if count%2==0: # 짝수
                dequeue.popleft()
            else:          # 홀수
                dequeue.pop()
        else:
            print('error')
            breaker=True
            break
        
    if breaker==True:
        pass
    elif count%2==0:
        print('['+','.join(dequeue)+']')
    else:
        dequeue.reverse()
        print('['+','.join(dequeue)+']')