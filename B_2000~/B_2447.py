# num을 1을 기준으로 놓느냐, 3을 기준으로 놓느냐의 차이

n=int(input())

def star(num):
    if num==1:
        return ['*']

    stars=star(num//3)
    case=[]

    for i in stars:
        case.append(i*3)
    for i in stars:
        case.append(i+' '*(num//3)+i)
    for i in stars:
        case.append(i*3)
    return case

for i in star(n):
    print(i)

# ---------------------------------------------------------------

n=int(input())

def star(num):
    if num==3:
        return ['***','* *','***']

    stars=star(num//3)
    case=[]

    for i in stars:
        case.append(i*3)
    for i in stars:
        case.append(i+' '*(num//3)+i)
    for i in stars:
        case.append(i*3)
    return case

for i in star(n):
    print(i)