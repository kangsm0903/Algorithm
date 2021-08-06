# 그룹 단어 체커
N = int(input())

word = [] # [['h','a','p','p','y'], ['n','e','w'], ['y','e','a','r']]

count = 0

for i in range(N):
    word.append(list(input()))

for i in word: # i == ['h','a','p','p','y']
    result = []
    location = []
    for l in i:
        result.append(list(filter(lambda x: i[x] == l, range(len(i))))) # [[0],[1],[2,3],[2,3],[4]]
    for k in result: # k = [0,1,3]
        if len(k) == 1:
            location.append(True)
        elif sum(k) > len(k)*(2*k[0]+(len(k)-1))//2:
            location.append(False)
        elif sum(k) == len(k)*(2*k[0]+(len(k)-1))//2:
            location.append(True)
    if False in location:
        pass
    else:
        count += 1

print(count)