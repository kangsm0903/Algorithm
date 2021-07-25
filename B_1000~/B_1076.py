N = [] # black red yellow

resister = [
    ['black',0,10**0],
    ['brown',1,10**1],
    ['red',2,10**2],
    ['orange',3,10**3],
    ['yellow',4,10**4],
    ['green',5,10**5],
    ['blue',6,10**6],
    ['violet',7,10**7],
    ['grey',8,10**8],
    ['white',9,10**9]
]

result = []

for i in range(0,3):
    N.append(input())

for k in range(0,2):
    for l in range(0,10):
        if N[k] == resister[l][0]:
            result.append(resister[l][1])

for m in range(0,10):
    if N[2] == resister[m][0]:
        result.append(resister[m][2])

end = int(str(result[0])+str(result[1]))*result[2]

print(end)
