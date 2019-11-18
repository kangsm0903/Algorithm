# 11/18 1110번

N = input()

N = int(N)

a = [] # 10미만
b = [] # 10이상

i = 1

if N // 10 == 0:
    a.append(0)
    a.append(N)
    a.append(N)

    while str(a[i]%10) + str(a[i+1]%10) != str(0)+str(N):
        d = (a[i]) + (a[i+1])
        a.append(d%10)
        i += 1
    print(i)
else:
    b.append(N//10)
    b.append(N%10)
    b.append((N//10) + (N%10))

    while str(b[i]%10) + str(b[i+1]%10) != str(N):
        c = (b[i]) + (b[i+1])
        b.append(c%10)
        i += 1
    print(i)

# 다른 풀이

# tmp = inp = int(input())

# count = 0

# while True:
#     ten = tmp // 10
#     one = tmp % 10
#     res = ten + one
#     count += 1
#     tmp = int(str(tmp%10) + str(res%10))

#     if (inp == tmp):
#         break
# print(count)