# 11/17 2920번

A = list(map(int,input().split()))

if A[0] == 1 and A[1] == 2 and A[2] == 3 and A[3] == 4 and A[4] == 5 and A[5] == 6 and A[6] == 7 and A[7] == 8:
    print('ascending')
elif A[0] == 8 and A[1] == 7 and A[2] == 6 and A[3] == 5 and A[4] == 4 and A[5] == 3 and A[6] == 2 and A[7] == 1:
    print('descending')
else:
    print('mixed')


# 모범답안
# if A ==  sorted(A):
#     print('ascending')
# elif A == sorted(A, reverse=True):
#     print('descending')
# else:
#     print('mixed')

#다른 풀이
# if A == [1,2,3,4,5,6,7,8]:
#     print('ascending')
# elif A == [8,7,6,5,4,3,2,1]:
#     print('descending')
# else:
#     print('mixed')