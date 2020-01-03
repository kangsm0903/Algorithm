B = input()

A = [str('c='),str('c-'),str('dz='),str('d-'),str('lj'),str('nj'),str('s='),str('z=')]

C = list(B) # [c,=,c,=]

D = 0

for i in A:
    while str(i) in B:
        z = list(i) # [c,=]
        for k in z:
            index = C.index(k)
            C[index] = '*'
            B = ''.join(C)
            y = C.count('*')
            for m in range(0,y):
                C.remove('*')
        D += 1
print(D + len(C))

# 모범답안 ----------------------------------------------------------------------------------------------

# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpha = input()

# for t in a:
#     alpha = alpha.replace(t, '*')

# print(len(alpha))