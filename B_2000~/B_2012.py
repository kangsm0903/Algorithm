# 예상등수[1,1,2,3,5] - 실제등수[1,2,3,4,5] = |[0,-1,-1,-1,0]| 절댓값 씌운 후 다 더하는 코드 
import sys
N=int(sys.stdin.readline()) # input() 대신 sys.stdin.readline()으로 조금이라도 시간단축을 위해 작성했음

A=[]
B=[i for i in range(1,N+1)] # B=[1,2,3,4,5] 실제등수
for i in range(N): 
    A.append(int(sys.stdin.readline())) # A=[1,1,2,3,5] 예상등수

A.sort() # 예상등수 정렬

total=0
for i in range(N):
    total+=abs(B[i]-A[i]) # Total = Total + |실제등수 - 예상등수|

print(total)

# --------------------------------------------------------------------------------------------------------
# 시간초과로 실패한 코드 1 - 연산이 많아서 시간초과인 것으로 판단됨
# B=[1,1,1,2,3,5], A=[-1,3,1,1,0,5] A가 인덱스 번호가 리스트 B에 몇개있는지 카운트한 것 ex) A[1]=3 B의 1이 3개, A[2]=1 B의2가 1개
import sys

N=int(sys.stdin.readline()) # 마찬가지로 input() 대신에 sys를 이용하여 시간단축을 하려했지만 시간초과

A=[0 for i in range(0,N+1)] # A=[0,0,0,0,0,0]
B=[] # [1,1,1,2,3,5]
for i in range(0,N):    # A=[0,3,1,1,0,5]
    num=int(sys.stdin.readline())
    B.append(num)
    A[num]+=1
A[0]=-1     # A=[-1,3,1,1,0,5] A[0]=1 이유는 아래에 A.index(0)에서 A[0]을 찾지않게 하기 위해서

total=0
for i in range(1,N+1): # 1~6 예상등수
    for k in range(1,A[i]): # A[i]만큼 반복 A[1]=3 이면 2번 나누어야하기에 2번 반복
        total+=abs(i-A.index(0)) # 불만도 계산
        A[A.index(0)]=1     # A.index(0)에 1을 나누었다고 보고 1 대입
        
print(total)

# --------------------------------------------------------------------------------------------------------
# 시간초과로 실패한 코드 2 - 연산이 많아서 시간초과인 것으로 판단됨
# 중복된 숫자와 비어있는 숫자를 빼서 불만도를 계산하는 과정으로 구현해봤음
N=int(input()) # 5
A=[int(input()) for i in range(N)] # A=[5,1,2,3,1]

B = []
for i in A: # B=[5,1,2,3] 중복 제거
    if i not in B:
        B.append(i)

for i in B: # A=[1] 중복값만 남김
    A.remove(i)

A.sort() # A=[1]   
B.sort() # B=[1,2,3,5]

C=[]
for i in range(1,N+1): # C=[4]
    try:
        if B[i-1]-i != 0: # B의 원소와 연속된 인덱스들의 차이가 0이 아니라면 C에 추가
            C.append(i)
    except IndexError:
        pass
C.sort(reverse=True)

D=(abs(x-y) for x,y in zip(A,C))

print(sum(D))