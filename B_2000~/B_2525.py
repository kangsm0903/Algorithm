Hour,Min=map(int,input().split())

time=int(input())

if (Min+time)//60>=1:
    Hour=Hour+(Min+time)//60
    Min=(Min+time)%60
    if Hour>=24:
        Hour=Hour-24
else:
    Min=Min+time

print(Hour, Min)