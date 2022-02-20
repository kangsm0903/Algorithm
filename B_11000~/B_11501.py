# 풀이참고함
# 주가를 앞에서부터가 아닌 뒤에서부터 비교하기 시작함
# 뒤에서부터 비교하여 현재의 최대값보다 현재의 인덱스의 값이 작으면 그 차익을 더하고 더 크면 그 값을 최대값으로 설정
import sys
 
Testcase=int(sys.stdin.readline()) # 테스트케이스
result=[]

for i in range(Testcase):
    N=int(sys.stdin.readline()) # 날의 수
    stock=list(map(int,sys.stdin.readline().split())) # stock=[1,1,3,1,2] 주가
    total=0
    M=0
    for k in range(N-1,-1,-1):
        if stock[k]>M:
            M=stock[k]
        else:
            total+=(M-stock[k])
    result.append(total)

for l in result:
    print(l)

# ----------------------------------------------------------------------------------------------------------
# 내 생각
# 주가를 앞에서부터 비교함
# 1. 주가의 최대값을 찾고 앞에서부터 차익을 더함
# 2. 최대값과 같은 값이 나오면 최대값을 0으로 할당함
# 3. 그 다음 최대값을 찾고 앞에서부터 차익을 더함 
T=int(sys.stdin.readline()) # 테스트케이스 개수
result=[]
for i in range(T): # 테스트케이스만큼 날짜와 주가를 받음
    N=int(sys.stdin.readline()) # 날의 수 3             2 <= N <= 1,000,000
    stock=list(map(int,sys.stdin.readline().split())) # 날 별 주가 10 7 6       stock<=10,000
    total=0
    for k in stock:
        M=max(stock)
        if k==M:
            stock[stock.index(k)]=0
        else: # stock[k] != M
            total+=(M-k)
    result.append(total)

for l in result:
    print(l)