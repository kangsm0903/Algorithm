import operator
# stages의 크기가 0인 것을 간과해서 런타임에러가 났던거라 판단됨
N = 0
stages = []

# print(stages.count(2)) # 3

A = {}
a = len(stages) # 8
b = []
for i in range(1,N+1):
    if a != 0:
        A[i] = (stages.count(i) / a)
        a -= stages.count(i)
    else:
        A[i] = 0
sorted_x = sorted(A.items(), key=operator.itemgetter(1), reverse=True)

for i in range(0,len(sorted_x)):
    b.append(sorted_x[i][0])
print(A)
print(b)

# key = operator.itemgetter(1) -> value값으로 정렬 / key = operator.itemgetter(0) -> key값으로 정렬
# lambda x,y : x+y == def add(x,y): return x+y

# 다른 풀이
# def solution(N, stages):
#     result = {} # A와 같은 역할로 추정
#     denominator = len(stages) # a와 같음
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage) # stages에서 1,2,3.. 개수를 count에 할당
#             result[stage] = count / denominator # dict형으로 실패율 할당
#             denominator -= count
#         else:
#             result[stage] = 0 # {0,0} stage가 0일때를 고려 안해서 그런듯
#     return sorted(result, key=lambda x : result[x], reverse = True)