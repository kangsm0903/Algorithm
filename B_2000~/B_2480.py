N=list(map(int, input().split())) # 3 3 6

M=set(N) # 3 6
 
if len(M)==3:
    print(max(M)*100)
elif len(M)==1:
    print(10000+max(M)*1000)
else: # len(M)==2
    for i in M:
        if N.count(i)==2:
            print(1000+i*100)