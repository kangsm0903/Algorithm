a=list(str(input()))
b=list(str(input()))

count=0

for i in range(len(a)):
    if a[i] in b:
        b.remove(a[i])
        count+=1
        
print(len(b)+(len(a)-count))