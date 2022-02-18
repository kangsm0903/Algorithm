N=int(input())
L=sorted(list(map(int,input().split())))
m=L[0]


if N==2:
    print(1)
else:
# N이 3이상
    for i in range(N): # 0~N-1 # 빈 공간 개수
        empty=len(L)-1-i    # 고리가 들어가야할 빈 공간의 개수 / 최솟값이 m에 하나 더 더해졌으니 빈 공간은 1개 더 줄어듬
        if m < empty: # 만약 빈 공간보다 최솟값이 작으면 최솟값 2개를 더해서 빈 공간보다 많게 만들어줌
            m+=L[i+1]
        else: 
            print(empty) # 빈 공간에 고리들을 할당해줌
            break