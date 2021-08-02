N = int(input())

result = []

for i in range(N):
    x1,y1,r1,x2,y2,r2 = map(float,input().split())

    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    # infinite
    if x1 == x2 and y1 == y2 and r1 == r2:
        result.append(-1)
    # 0 point
    elif r1 + r2 < d:
        result.append(0)
    elif d+min(r1,r2)<max(r1,r2) and min(r1,r2)<max(r1,r2):
        result.append(0)
    # 1 point
    elif r1 + r2 == d:
        result.append(1)
    elif d+min(r1,r2) == max(r1,r2):
        result.append(1)
    else:
        result.append(2)

for i in result:
    print(i)