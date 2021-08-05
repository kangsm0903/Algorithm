x, y = map(int, input().split())

a = list(str(x)) # [1,0,0,1,0]
b = list(str(y))

sub = []
sub2 = []
result = []

for i in range(len(a)-1,-1,-1):
    sub.append((2**i)*int(a[-(i+1)]))

for l in range(len(b)-1,-1,-1):
    sub2.append((2**l)*int(b[-(l+1)]))

sub_result = sum(sub) + sum(sub2)

while True:
    if sub_result < 2:
        result.append(sub_result)
        break
    result.append(sub_result%2)
    sub_result = sub_result // 2

result.reverse()

print("".join([str(i) for i in result]))

# a, b= map(str, input().split())

# x = list(a)
# y = list(b)

# c = int(a)
# d = int(b)

# result = []
# sub = []

# if len(a) != len(b):
#     for k in range(max(len(a),len(b))-min(len(a),len(b))):
#         sub.append(max(a,b)[k])
#         max(a,b).remove(max(a,b)[k])

# for i in range(1, max(len(x),len(y))+1):
#     if int(x[-i]) + int(y[-i]) == 2:
#         try:
#             x[-(i+1)] = int(x[-(i+1)]) + 1
#             result.append(0)
#         except IndexError:
#             result.append(0)
#             result.append(1)
#     elif int(x[-i]) + int(y[-i]) == 1:
#         result.append(1)
#     elif int(x[-i]) + int(y[-i]) == 3:
#         try:
#             x[-(i+1)] = int(x[-(i+1)]) + 1
#             result.append(1)
#         except IndexError:
#             result.append(1)
#             result.append(1)
    

# print(result)
# result.reverse()