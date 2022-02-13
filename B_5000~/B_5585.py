A=1000-int(input())
B=[500,100,50,10,5,1]
count=0
for i in B:
    count+=A//i
    A=A%i
print(count)