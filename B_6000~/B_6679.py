def controler(n,q): # q진수 변환기
    base=0
    while n>0:
        n, mod=divmod(n,q)
        base+=mod # 나머지들 합산

    return base 

for i in range(1000,10000):
    A=controler(i,12)
    B=controler(i,16)
    C=[int(l) for l in list(str(i))]
    if A==B and B==sum(C):
        print(i)
    