a=[]
a.append(input())
add=0
b=a[0].split("-")
for i in range(1,len(b)):
    if b[i].find("+")!=-1:
        c=b[i].split("+")
        for k in range(0,len(c)):
            c[k]=int(c[k])
        add+=sum(c)
    else:
        add+=int(b[i])

if b[0].find("+")!=-1:
    d=b[0].split("+")
    for i in range(0,len(d)):
        d[i]=int(d[i])
    d=sum(d)
else:
    d=int(b[0])

total = (add*-1)+d
print(total)
