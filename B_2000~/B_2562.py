# 11/16 2562번

b = []

for i in range(0,9):
    a = input()
    a = int(a)
    b.append(a)

print(max(b))
print(b.index(max(b))+1)
