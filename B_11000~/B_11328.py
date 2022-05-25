# 두 개를 list 형태로 받아 sort로 알파벳 순으로 정렬하고
# 다시 문자열로 바꿔서 같으면 Possible 아니면 Impossible
N=int(input())

result=[]

for i in range(N):
    case1,case2=map(str,input().split(" "))
    first=sorted(list(case1))
    second=sorted(list(case2))
    if ",".join(first)==",".join(second):
        result.append("Possible")
    else:
        result.append("Impossible")

for i in result:
    print(i)

# ---------------------------------------
# Counter - 단어에 포함된 알파벳의 글자 수를 dict로 세어주는 간단한 함수
# hello world = {'h':1,'e':1,'l':3,'o':2,' ': 1, 'w':1,'r':1,'d':1}
from collections import Counter

N=int(input())

for i in range(N):
    a,b=map(str,input().split())

    if Counter(a)==Counter(b):
        print('Possible')
    else:
        print('Impossible')