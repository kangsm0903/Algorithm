# 평행사변형
x1,y1,x2,y2,x3,y3 = map(float,input().split())

if x1==x2 and x2==x3:
    print(-1.0)
elif y1==y2 and y2==y3:
    print(-1.0)    
else:
    try:
        deltaA = abs(y1-y2)/abs(x1-x2)  
        deltaB = abs(y2-y3)/abs(x2-x3)
        if deltaA == deltaB:
            print(-1.0)
    except ZeroDivisionError:
        pass

line = []

line.append(((x1-x2)**2+(y1-y2)**2)**(1/2)) # (x1,y1) - (x2,y2)
line.append(((x2-x3)**2+(y2-y3)**2)**(1/2)) # (x2,y2) - (x3,y3)
line.append(((x1-x3)**2+(y1-y3)**2)**(1/2)) # (x1,y1) - (x3,y3)

line = sorted(line)

big = (line[2]+line[1])*2
small = (line[1]+line[0])*2

print(big-small)