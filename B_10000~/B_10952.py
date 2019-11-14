# 11/14 10952번
c = []
a = 1
b = 1

while a and b != 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    c.append(a+b)

for i in range(0, len(c)-1):
    print(c[i])