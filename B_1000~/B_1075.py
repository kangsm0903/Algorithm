N = int(input())
F = int(input())

first = N // 10**2

purpose = first * 100

target = purpose // F # 333

result = target * F # 999

while result < purpose:
    result = result + F

A = list(str(result))

print(A[-2]+A[-1])