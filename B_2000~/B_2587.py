case=[]

for i in range(5):
    case.append(int(input()))

case.sort()
print(sum(case)//5)
print(case[2])