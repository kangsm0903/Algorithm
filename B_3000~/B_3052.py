# # 11/20 3052번

A = []

for i in range(0,10):
    A.append(int(input()) % 42)

for i in range(0,10):
    if A.count(A[i]) >= 2:
        A[i] = 'algorithm'
    else:
        pass

B = A.count('algorithm')

for i in range(0,B):
    A.remove('algorithm')

print(len(A))


# 다른 괜찮은 풀이
# num_list = []
# rem_list = []

# for i in range(10):
#     num_list.append(int(input()))

# for num in num_list:
#     rem = num % 42
#     if rem in rem_list:
#         pass
#     else:
#         rem_list.append(rem)