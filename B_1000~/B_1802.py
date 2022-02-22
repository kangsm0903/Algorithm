# 접는 부분 양 옆이 다른지 확인 + 대칭되는 인덱스 원소의 값이 다른지 확인
import sys

Testcase=int(sys.stdin.readline()) # T<=1000

total=[]

for i in range(Testcase):
    N=list(str(sys.stdin.readline().rstrip('\n'))) # ['1','0','0','0','1','1','0']
    if len(N)==1:
        result='YES'
    for k in range(1,len(N),2): # 접는 부분 양 옆이 다른지 확인
        if N[k-1]!=N[k+1]:
            if k==len(N)-2:
                result='YES'
            else:
                pass
        else: # N[k-1]==N[k+1]
            result='NO'
            break

    for k in range(len(N)): # 대칭되는 인덱스 원소의 값이 다른지 확인
        if k==(len(N)//2):
            result2='YES'
            break
        elif N[k]==N[-(k+1)]:
            result2='NO'
            break
    if result==result2:
        total.append(result)
    else:
        total.append('NO')

for l in total:
    print(l)

# ------------------------------------------------------------------------------------------------
# 0000111 <- 이 반례를 고려하지 못했음
import sys

Testcase=int(sys.stdin.readline()) # T<=1000
result=[]

for i in range(Testcase):
    N=list(str(sys.stdin.readline().rstrip("\n"))) # N<3000, 문자열 길이 홀수
    middle=len(N)//2 # 

    if middle==0:
        result.append('YES')
    else:
        A=N[:middle]
        A=int("".join(A)) # 0101

        B=(N[middle+1:])
        B.reverse()
        B=int("".join(B)) # 1010

        if A+B==int('1'*middle):
            result.append('YES')
        else:
            result.append('NO')

for k in result:
    print(k)

# ------------------------------------------------------------------------------------------------
# 0000111 <- 이 반례를 고려하지 못했음
import sys

Testcase=int(sys.stdin.readline()) # T<=1000
result=[]

for i in range(Testcase):
  N=list(str(sys.stdin.readline().rstrip('\n'))) # ['1','0','0','0','1','1','0']
  middle=len(N)//2
  for k in range(len(N)):
    if k==middle:
      result.append('YES')
      break
    elif N[k]==N[-(k+1)]:
      result.append('NO')
      break
    else:
      pass

for l in result:
  print(l)