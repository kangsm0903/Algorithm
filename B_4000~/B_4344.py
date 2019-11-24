# 11/24 4344번

N = int(input()) # 테스트 케이스 

A = []
B = []
C = []

# N = 3

for i in range(0,N):
    A.append(list(map(int, input().split())))

# A [[5 50 50 70 80 100],[3 70 90 80],[3 70 90 81]]

for i in range(0,N):
    B.append((sum(A[i])-A[i][0])/A[i][0]) # 평균값
    A[i].remove(A[i][0]) # 학생 수 제거

print(A) # A = [[50 50 70 80 100], [70 90 80], [70 90 81]]
print(B) # B = [70, 80, 80.333]

for i in range(0,N):
    C.append([]) # C에 빈 배열 추가
    for k in A[i]:
        if k > B[i]:
            C[i].append(k) # 80 100 ~
        else:
            pass

print(C)

for i in range(0,N):
    print(str('%.3f' % (len(C[i])/len(A[i])*100)) + '%')