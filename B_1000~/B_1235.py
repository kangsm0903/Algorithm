# case[k][i:]를 이용하여 k번째 인덱스부터 마지막 인덱스까지 join으로 묶어 문자열로 만들어줌
# 묶어준 문자열을 Allin이라는 set집합에 넣어주고 집합의 개수가 N과 같은 지 비교
# set집합에서 겹치는 것이 존재하면 set의 개수와 N이 같을 수가 없음
# set집합의 원소 갯수와 N이 같을 때까지 반복문을 돌리면서 찾는다.

import sys

N=int(sys.stdin.readline().rstrip('\n'))

case=[]

for i in range(N):
    case.append(list(str(sys.stdin.readline().rstrip('\n'))))

for i in range(len(case[0])-1,-1,-1):
    Allin=set([])
    for k in range(N):
        Allin.add(''.join(case[k][i:]))
    if len(Allin)==N:
        result=i
        break

print(len(case[0])-result)
# 문자열 길이 - 앞 기준 문자열 인덱스 = 뒤 기준 문자열 인덱스