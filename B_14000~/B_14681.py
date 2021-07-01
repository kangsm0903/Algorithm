# 2021/07/01 14681 사분면 고르기

X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    print(int(1))
elif X < 0 and Y > 0:
    print(int(2))
elif X < 0 and Y < 0:
    print(int(3))
else:
    print(int(4))