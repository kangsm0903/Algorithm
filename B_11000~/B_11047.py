a,b=input().split(" ")
c=[]
count=0
for i in range(int(a)):
    c.append(int(input()))

for i in range(int(a),0,-1):
    if int(b)==0:
        break
    elif int(b)%c[i-1]==int(b):
        pass
    else:
        count=count+(int(b)//c[i-1])
        b=int(b)%c[i-1]

print(count)