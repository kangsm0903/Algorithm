A = []
B = 1

while B != ['0']:
    B = list(str(input()))
    A.append(B)

for i in A:
    C = list(reversed(i))
    x = "".join([str(l) for l in i])
    y = "".join([str(l) for l in C])
    if x == '0' or y == '0':
        break
    elif x == y:
        print('yes')
    elif x != y:
        print('no')
