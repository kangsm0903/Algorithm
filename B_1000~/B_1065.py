# 12/08 1065번
# 0. 만약 N < 100 이면 return N(1~N까지 한수이기에) N>=100이면 이때부터 한수 체크
# 1. 1 ~ N 까지 정렬
# 2. 1 ~ N 사이의 하나의 수 M을 자릿수별로 나누기
# 3. 각 자릿수의 차이가 일정하다면 = 한수

N = int(input())

A = []
D = []
if N >= 100:
    for i in range(100, N+1): # 100 ~ N+1 까지 정렬
        A.append(i)

    for k in range(0, len(A)):
        M = A[k]
        B = []
        for m in range(len(str(A[k]))-1, -1, -1): # len(A[k])-1 ~ 0까지 -1씩 감소
            B.append(M // 10**m) # 몫
            M = M % 10**m # 나머지

        diff = B[0] - B[1] # 기준이 되는 등차
        C = []
        for l in range(1, len(B)-1): # 각 자리별 등차가 기준과 같은지 비교
            if B[l] - B[l+1] == diff: # 같다면 True를 넣고 다르면 False를 넣음
                C.append(True)
            else:
                C.append(False)
        
        if False in C: # 만약 list속에 False가 하나라도 있으면 pass 모두 True라면 list속에 넣음
            pass
        else:
            D.append(A[k])

    print(len(D)+99)
else:
    print(N)