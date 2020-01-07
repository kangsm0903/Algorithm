# 2020/01/07 1085번

N = list(map(int, input().split()))

M = []

M.append(N[2]-N[0]) # x
M.append(N[3]-N[1]) # y
M.append(N[0]-0)
M.append(N[1]-0)

# print(M)
print(min(M))