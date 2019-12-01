#  12/02 10951번
c = []

try:
    while True:
        a, b = map(int, input().split())
        c.append(a+b)
except:
    for i in range(0,len(c)):
        print(c[i])

# try / except try에 에러가 뜰 수 있는 구문을 넣고 except에 에러가 떳을 시 실행할 명령을 입력한다.
# 여기서는 아무것도 입력하지 않은 것(not enough values to unpack)이 에러로 볼 수 있다. 

# --------------------------------------------------------------

# i = 0
# B = [1]

# while sum(B[i]) > 0:
#     A = list(map(int, input().split()))
#     i = i + 1
#     B.append(A)

# for i in range(1, len(B)-1):
#     print(sum(B[i]))

# i = 0
# B = []

# while i != 6:
#     A = list(map(int, input().split()))
#     i = i + 1
#     B.append(A)

# for i in range(1 , len(B)+1):
#     print(sum(B[i-1]))


# C = [[1,2,3], [3,5,7]]
# print(sum(C[1]))

# a = [0,1,2,3,4,5,6,7,8,9]

# print(a[1])

# while sum(a[1]) == 0:
#     print('possible?')


# first = 0
# A = [[1,1]]

# while sum(A[first]) != 0:
#     A.append(list(map(int, input().split())))
#     first += 1

# for i in range(1, len(A)-1):
#     print(sum(A[i]))
