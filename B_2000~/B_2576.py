case=[]
case2=[]

for i in range(7):
    case.append(int(input()))

for i in case:
    if i%2==1:
        case2.append(i)
if case2==[]:
    print(-1)
else:
    print(sum(case2))
    print(min(case2))