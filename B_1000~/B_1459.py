X,Y,W,S = list(map(int,input().split(" "))) # X,Y,W,S

M = max(X,Y)
m = min(X,Y)

if 2*W < S:
    print((X+Y)*W)
elif 2*W > S:
    if W < S:
        print(m*S+(M-m)*W)
    elif W > S:
        if (M-m)%2==1: # (M-m)이 홀수일 때
            print(m*S+(M-m-1)*S+W)
        else: # (M-m)이 짝수일 때
            print(m*S+(M-m)*S)
    else: # W = S
        print(m*S+(M-m)*W)
else: # 2W = S
    print(m*S+(M-m)*W)


#-------------------------------------------------------------------------------------------------
# 제너레이터 등을 이용해서 최대한 메모리를 줄어보려했지만 메모리초과로 계속 실패

# A = list(map(int,input().split())) # X,Y,W,S

# straight = sum(A[0:2])
# M = max(A[0],A[1])
# m = min(A[0],A[1])

# st=[]
# for i in range(m+1):
#     st.append(straight)
#     straight-=2

# if A[2] <= A[3]:
#     distan = (i*A[3]+st[i]*A[2] for i in range(m+1))
#     print(min(distan))
# else:
#     if (M-m)%2==1: # 홀수
#         print(m*A[3]+(M-m-1)*A[3]+A[2])
#     else:
#         print(m*A[3]+(M-m)*A[3])