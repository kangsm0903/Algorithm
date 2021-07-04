# 2021/07/02 2869 달팽이는 올라가고 싶다
# 시간초과로 인한 실패..

import math

N = list(map(int, input().split()))

A = N[0] # up 
B = N[1] # down
V = N[2] # length

day = (V-B)/(A-B)

print(math.ceil(day))

# while True:
#     height += A
#     count += 1
#     if height >= V:
#         break
#     height -= B