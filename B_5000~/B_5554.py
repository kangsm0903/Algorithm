N = []

for i in range(0,4):
    N.append(int(input()))

print(int(sum(N)/60))
print(sum(N)%60)