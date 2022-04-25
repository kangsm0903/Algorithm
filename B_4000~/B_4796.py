import sys

result=[]

while True:
    case=list(map(int,sys.stdin.readline().split()))
    if sum(case)==0:
        break
    num=case[2]//case[1]*case[0]
    if case[2]%case[1]<=case[0]:
        num+=case[2]%case[1]   
    else:
        num+=case[0]
    result.append(num)

for i in range(len(result)):
    k=i+1
    print("Case {idx}: {val}".format(idx=k, val=result[i]))