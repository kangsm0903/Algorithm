# python 2588번
# 값들을 list에 넣고 해야할 듯 
a = list(input())
b = list(input())

a.append(a[0]+a[1]+a[2])
b.append(b[0]+b[1]+b[2])

print(int(a[3])*int(b[2]))
print(int(a[3])*int(b[1]))
print(int(a[3])*int(b[0]))
print(int(a[3])*int(b[3]))