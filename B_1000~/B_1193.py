# 2020/01/08 1193번 분수찾기

N = int(input())

A = 0
B = 1

count = 1
floor = 1

while True:
    if A < N <= B:
        break
    else:
        A = B
        count += 1
        B += count
    floor += 1

distant = N - (A+1)

if floor % 2 == 0: # 짝수면
    C = str(1+distant) + '/' + str(floor-distant)
else: # 홀수면
    C = str(floor-distant) + '/' + str(1+distant)

print(C)