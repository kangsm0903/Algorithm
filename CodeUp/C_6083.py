a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
count = 0
for i in range(0,a):
    for l in range(0,b):
        for k in range(0,c):
            print(i,l,k)
            count+=1

print(count)