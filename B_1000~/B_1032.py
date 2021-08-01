N = int(input())

A = []

if N == 1:
    A.append(input())
    print(A[0])
else:
    for i in range(0,N):
        A.append(list(input()))
        
    count = 0

    for i,j in zip(A[0],A[1]):
        if i != j:
            A[0][count] = '?'
        count += 1

    for k in range(2,N):
        number = 0
        for i,j in zip(A[0],A[k]):
            if i != j:
                A[0][number] = '?'
                # print(number)
                # print(A[0])
            number += 1
        
    print("".join(A[0]))