w,h,b=input().split()
w=int(w)
h=int(h)
b=int(b)
storage=w*h*b
print("{:.  2f}".format(storage/8/1024/1024),end=" ")
print("MB")
