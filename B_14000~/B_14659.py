# O(N)
import sys

N=int(sys.stdin.readline()) # 7

case=list(map(int,sys.stdin.readline().split())) # 6 4 10 2 5 7 11

result=[]

while len(case)!=0:        # case가 다 비어질 때까지 반복
    M=max(case)            # 봉우리의 최댓값을 받아줌
    if case.index(M)==N-1: # 만약 최댓값이 리스트의 맨 끝에 있다면
        result.append(0)   # 결과에 0을 반환하고
        case.remove(M)     # 리스트에서 최댓값을 삭제
    else:                                          # 맨 끝에 있는 것이 아니라면
        result.append(len(case[case.index(M):])-1) # 최댓값부터 맨 끝까지의 갯수-1 을 카운팅 후 반환 
        del case[case.index(M):]                   # 최댓값부터 맨 끝까지의 원소들을 삭제

print(max(result)) # 결과값의 최댓값을 반환

# ----------------------------------------------------------------------------------------------
# O(n^2)
import sys

N=int(sys.stdin.readline())

case=list(map(int,sys.stdin.readline().split()))

result=[]

for i in range(0,len(case)):
    cnt=0
    for k in range(i+1,len(case)):
        if case[i]<case[k]:
            break
        else:
            cnt+=1
    result.append(cnt)

print(max(result))