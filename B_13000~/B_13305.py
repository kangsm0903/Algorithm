#O(n) 시간복잡도를 고려해서 작성함 100점
N=int(input()) # 5
distance=list(map(int, input().split( ))) # [5,3,2,1]
price=list(map(int, input().split( ))) # [3,4,2,2,3]

total = price[0]*distance[0]
mprice=price[0]

for i in range(N-1): # 0,1,2
    try:
        if mprice <= price[i+1]:    # 이전 값이 더 작을 때
            pass
        else:                           # 이후 값이 더 작을 때
            mprice=price[i+1]
        total = total + mprice*distance[i+1]
    except IndexError:
        print(total)


# 최솟값이 갱신되는 것을 고려하지않았음. 17점
total = price[0]*distance[0]
for i in range(N-1):
    try:
        if price[i]<=price[i+1]:
            total = total + price[i]*distance[i+1]
        elif price[i]>price[i+1]:
            total = total + price[i+1]*distance[i+1]
    except IndexError:
        print(total)
    
# while 때문에 시간이 많이 걸리는 것으로 보임
pay=[]
while len(price)!=0:
    A=price.index(min(price)) # 2, 0

    # 최솟값을 구하고 그 뒤에 도로거리들의 합
    total = sum(distance[A:])

    pay.append(total*price[A]) # 최솟값 기준 뒤의 도로거리 * 최솟값 

    # 최솟값 포함해서 뒤에 값들 삭제
    del price[A:]
    del distance[A:]

print(sum(pay))
