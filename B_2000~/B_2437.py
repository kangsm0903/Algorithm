import sys 

N=int(sys.stdin.readline()) # 저울 개수

case=list(map(int,sys.stdin.readline().split()))

case.sort() # 1,1,2,3,6,7,30 오름차순 정렬

now=case[0] 

if now!=1: # 맨 처음 최솟값이 1이 아니라면 측정할 수 없는 값이 1이기에 1 반환 
    print(1)
else: # now+1과 같거나 작으면 구간 증가
    for i in range(1,N):
        if now+1 >= case[i]:
            now+=case[i]
        else: # 조건에 맞지 않다면 break하고 now+1 출력 (now까지는 측정할 수 있기에)
            break
    print(now+1)