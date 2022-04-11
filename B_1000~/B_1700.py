# 멀티탭에 빈자리가 있으면 꽂기
# 멀티탭에 빈자리가 없을 경우
# 1. 멀티탭에 겹치는 번호가 있다면 그대로 두기
# 2. 멀티탭에 겹치는 번호가 없다면 
# 2-1. 나중에 쓸 일이 없는 플러그를 뽑기
# 2-2. 가장 나중에 사용할 플러그를 뽑기

import sys

N, K= map(int,sys.stdin.readline().split()) # N 멀티탭 구멍 / K 전기용품 사용 횟수

case=list(map(int,sys.stdin.readline().split())) # 2 3 2 3 1 2 7

tab=[] # 멀티탭 상황
count=0

for i in range(len(case)):
    if case[i] in tab: # 멀티탭에 겹치는 번호가 있다면 그대로 두기
            pass
    else:
        if len(tab)<N: # 멀티탭에 자리가 남아 있을 경우
            tab.append(case[i])
        else:
            compare=[]
            for k in range(len(tab)): # 멀티탭에 있는 것들이 case에서 인덱스 몇을 가지는 지 확인
                if case[i+1:].count(tab[k])==0: 
                    compare.append(101) # case에 나중에 쓸 멀티탭이 없다면 101 추가
                else:
                    A=case[i+1:].index(tab[k]) # 있으면 인덱스 추가
                    compare.append(A)
            del tab[compare.index(max(compare))] # 최댓값의 인덱스 번호의 tab을 삭제
            tab.append(case[i]) 
            count+=1

print(count)