# 2020/01/06 2292번 벌집

N = int(input())

count = 1

first = 2

while True:
    if N == 1:
        break
    elif first <= N < 6*count + first:
        count += 1
        break
    else:
        first = 6*count + first
        count += 1 

print(count)