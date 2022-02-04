a=[]
a.append(input())
add=0
b=a[0].split("-")   # - 기준으로 분리
for i in range(1,len(b)):   
    if b[i].find("+")!=-1:  # ["50","40+30"] 처럼 + 존재 시 + 기준으로 분리 후 합함
        c=b[i].split("+")
        for k in range(0,len(c)):
            c[k]=int(c[k])
        add+=sum(c)
    else:   # ["50", "30"] 처럼 존재 시 정수로 타입만 바꿈
        add+=int(b[i])

if b[0].find("+")!=-1: # b[0] 에서 + 존재 시 + 기준으로 분리 후 합함
    d=b[0].split("+")
    for i in range(0,len(d)):
        d[i]=int(d[i])
    d=sum(d)
else:   # + 없으면 정수로 타입만 바꿈
    d=int(b[0])

total = (add*-1)+d
print(total)
