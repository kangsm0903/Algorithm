import math
# O(n)
# 여자 0 /  남자 1 / 학년
male=[0,0,0,0,0,0] # 최대 6학년이기에 6개
female=[0,0,0,0,0,0]

n,k=map(int,input().split()) # n 최대 1000, k 최대 1000
total=0

for i in range(n):
    sex, grade=map(int,input().split())
    if sex==0: # 성별이 여자면 여자[학년]+=1
        female[grade-1]+=1
    else: # 성별이 남자면 남자[학년]+=1
        male[grade-1]+=1

# 각각의 값을 나누고 올림하여 total에 누적합
for i in male:
    total+=math.ceil(i/k)

for i in female:
    total+=math.ceil(i/k)

print(total)