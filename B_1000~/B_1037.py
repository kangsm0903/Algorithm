Number = int(input())

test = list(map(int, input().split()))

answer = []

if len(test) == 1:
    answer.append(test[0]**2)
else:
    answer.append(max(test)*min(test))

print(answer[0])