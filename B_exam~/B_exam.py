# 창영이와 점프

N = list(map(int, input().split()))

L = list(map(int, input().split()))

count = 0 
jump = 0

for i in sorted(L):
    if i <= N[1]:
        count += 1
    elif i > N[1] and jump == 1:
        break
    else:
        jump += 1
        count += 1

print(count+1)