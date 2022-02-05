# 58점 O(n^2) 시간복잡도를 고려해서 다시 작성해볼 것
N=int(input()) # 5
road=list(map(int, input().split( ))) # [5,3,2,1]
city=list(map(int, input().split( ))) # [3,4,2,2,3]

pay=[]
while len(city)!=0:
    total=0
    A=city.index(min(city)) # 2, 0

    for i in range(A,len(road)): # 최솟값을 구하고 그 뒤에 도로거리들의 합
        total+=road[i] # total = 2 + 1

    pay.append(total*city[A]) # 최솟값 기준 뒤의 도로거리 * 최솟값 

    for i in range(A,len(city)): # 최솟값 포함해서 뒤에 값들 삭제
        del city[A]

    for i in range(A,len(road)):
        del road[A]
    
print(sum(pay))
