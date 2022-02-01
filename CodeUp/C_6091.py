a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
d=1
while d%a!=0 or d%b!=0 or d%c!=0: # 거짓일때 멈춤 = 다 거짓이여야 멈춤
    d+=1
print(d)