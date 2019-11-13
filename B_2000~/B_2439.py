# 11/13 2439번

N = input()
N = int(N)
a = '*'
for i in range(1,N+1):
    print(("*" * i).rjust(N))