# 핸드폰 요금
import math

N=int(input())

case=list(map(int,input().split()))

pay1=0
for i in case:
    if i%30==0:
        pay1+=(math.ceil(i/30)+1)*10
    else:
        pay1+=math.ceil(i/30)*10

pay2=0
for i in case:
    if i%60==0:
        pay2+=(math.ceil(i/60)+1)*15
    else:
        pay2+=math.ceil(i/60)*15

if pay1>pay2:
    print('M', end=' ')
    print(pay2)
elif pay1<pay2:
    print('Y', end=' ')
    print(pay1)
else:
    print('Y M',end=' ')
    print(pay1)