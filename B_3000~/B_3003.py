N = list(map(int, input().split()))
M = [1,1,2,2,2,8]
result = 'first'

for i in range(0, len(M)):
    result = result + ' ' + str(M[i]-N[i])

result = result.replace('first ', '')

print(result)