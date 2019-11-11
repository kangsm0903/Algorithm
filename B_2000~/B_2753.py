# 2753번

a = input()

a = int(a)

if 1 == ((a%4==0 and a%100!=0) or (a%4==0 and a%400 ==0)):
    print(1)
else:
    print(0)