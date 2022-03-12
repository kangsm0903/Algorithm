# 음수, 양수로 나누고 음수는 오름차순, 양수는 내림차순으로 정렬
# [-39,-37,-29,-28,-6][11,2]
# 책을 M개씩 가지고 갈 수 있음 - list[0:M] 0~M-1개로 M개 중 절댓값의 최대값을 뽑아냄 (ex.[-39,-37]이라면 39를 뽑아냄)
# 위에서 뽑아낸 최대값을 *2해서 total에 할당(왔다갔다 왕복거리), 기존 케이스에서 0~M-1 삭제
# 이걸 반복
# total에 왕복거리들이 할당되어있는데 그것들 중 최대값을 마지막으로 생각하고 편도로 설정 - 최대값//2
# total 합하기

import math
import sys

N,M=map(int,sys.stdin.readline().split())

case=list(map(int,sys.stdin.readline().split()))

odd=[]
even=[]
total=[]

for i in case:
    if i>0:
        even.append(i)
    else:
        odd.append(i)

odd.sort() # 오름차순으로 정렬
even.sort(reverse=True) # 내림차순으로 정렬

for i in range(math.ceil(len(odd)/M)): # 음수 케이스[:M] 중 최솟값을 total에 할당
    total.append(abs(min(odd[:M]))*2)
    del odd[:M] # 할당 후 삭제

for i in range(math.ceil(len(even)/M)):# 양수 케이스[:M] 중 최대값을 total에 할당
    total.append(abs(max(even[:M]))*2)
    del even[:M] # 할당 후 삭제

total[total.index(max(total))]=max(total)//2 # 최종 왕복 거리들 중 최댓값을 마지막 거리로 생각하여 편도로 설정
print(sum(total))