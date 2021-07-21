import math

N = int(input())

number = []
problem = []

for i in range(0, N):
    number.append(list(map(int, input().split())))
    number[i].append(number[i][1]-number[i][0])
    problem.append(int(math.factorial(number[i][1]) / (math.factorial(number[i][0])*math.factorial(number[i][2]))))

for k in range(0, len(problem)):
    print(problem[k])