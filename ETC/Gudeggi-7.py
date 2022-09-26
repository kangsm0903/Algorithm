floor=int(input()) # 만나면 안되는 층
count=int(input()) # 만나면 안되는 횟수

if floor==5 or floor==1:
    result=count*8
else:
    result=count*4

if count%2==1: #홀수
    result+=5-floor
else: #짝수
    result+=floor-1

print(result)