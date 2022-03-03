# 원래는 0,1의 갯수를 기준으로 많은 갯수가 반복되는 것도 많을 줄 알았는데 아니였음
# 그래서 0,1 모두 최소횟수를 카운트하고 둘 중에서 최소횟수를 가려냈음
import sys

M=(str(sys.stdin.readline().rstrip('\n'))) # M
N=list(M) 

count1=0
count2=0
try:
    for i in range(len(N)):
        if i==(len(N)-1) and N[i]=='0':
            count1+=1
        elif N[i]!=N[i+1] and N[i]=='0':
            count1+=1
        else:
            pass
except IndexError:
    pass

try:
    for i in range(len(N)):
        if i==(len(N)-1) and N[i]=='1':
            count2+=1
        elif N[i]!=N[i+1] and N[i]=='1':
            count2+=1
        else:
            pass
except IndexError:
    pass

print(min(count1,count2))