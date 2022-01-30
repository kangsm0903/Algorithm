h,b,c,s=input().split(" ")
h=float(h)
b=float(b)
c=float(c)
s=float(s)
bit=h*b*c*s
print("{:.1f}".format(bit/8/1024/1024), end=" ")
print("MB")