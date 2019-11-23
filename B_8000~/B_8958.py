# 11/22 8958번

N = int(input())

A = {}

for i in range(0,N):
    A[i] = input().split('X')

C = []

for i in range(0,N):
    C.append([])
    for k in range(0,len(A[i])):
        B = len(A[i][k])
        C[i].append((B*(B+1)/2)) # 시그마 n 을 사용함 

for i in range(0,N):
    print(int(sum(C[i])))

# 하나의 key값에 다수의 value값을 넣어볼라고 setdefault, default를 써봤지만 좀더 공부해야할 듯
# B = {}

# for i in range(0,N):
#     for k in range(0,len(A[i])):
#         P = len(A[i][k])
#         if i in B:
#             B.setdefault(i,[]).append(P(P+1)/2)
#         else:
#             B[i] = (P*(P+1)/2)
        
# print(B) 