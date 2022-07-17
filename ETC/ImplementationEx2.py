# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 ㅗ학인
# Brute Force (하루 == 86,400초이기에 컴퓨터는 충분히 계산가능)

N=int(input())

cnt=0

for h in range(N+1):
    if '3' in str(h):
        cnt+=3600 
        continue
    for m in range(60):
        if '3' in str(m):
            cnt+=60
            continue
        for s in range(60):
            if '3' in str(s):
                cnt+=1
                continue

print(cnt)

# -------------------------------------------------

h=int(input())

count=0

for h in range(h+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count+=1

print(count)