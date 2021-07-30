N = int(input())

A = list(map(int, input().split()))

primes = []

for i in range(0,1001): # 0~1000
    result = True
    if i < 2:
        result = False
    else:
        for j in range(2,i):
            if i%j == 0:
                result = False
        if result:
            primes.append(i)

count = 0

for k in range(0,N):
    if A[k] in primes:
        count += 1

print(count)