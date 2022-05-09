import sys

N=int(sys.stdin.readline()) # 13

case=set([]) # 처음에 set집합으로 중복을 없애줌

for i in range(N): # set집합에 데이터들 넣어줌
    case.add(str(sys.stdin.readline()).rstrip('\n'))

case=sorted(list(case)) # 중복값을 없앤 set집합을 list로 변환하고 정렬해줌

# filter(조건함수, 순회가능 데이터)
for i in range(1,51):
    for k in filter(lambda x:len(x)==i,case): # case의 원소들이 1~50 길이인 것들을 필터링함
        print(k)