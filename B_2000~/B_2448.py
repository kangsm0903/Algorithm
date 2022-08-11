# 기존의 삼각형을 담아줄 변수 result를 전역변수로 설정하여 구현하였다.
# case에는 이전 재귀에서 넘어온 도형의 복제본들만 넣어주고
# result에 담긴 기존의 도형과 case를 합쳐서 반환해준다. 22번줄

# 삼각형 사이의 공백은 (num-1)=='*'과 '*' 사이의 공백 간격
# (num-1-(2*i))는 삼각형의 간격이 2씩 줄어들기에 i가 1씩 커지는 변수를 이용하여 공백을 구현

n=int(input())

result=[]

def star(num):
    global result
    if num==3:
        result.append('*') # 기존의 삼각형들을 result에 넣어줌
        result.append('* *')
        result.append('*****')
        return ['*','* *','*****']

    stars=star(num//2) 
    case=[]

    for i in range(len(stars)): # result로 만들어진 삼각형들을 case에 넣어줌
        case.append(stars[i]+' '*(num-1-(2*i))+stars[i])
    result=result+case # 기존+새로운 삼각형 = result에 담아줌
    return result

star(n)

for i in range(n-1,-1,-1): # result의 맨 뒤에서부터 띄어쓰기 공백을 넣어줌
    space=(n-i-1)*' '
    # 문제의 특징으로 앞의 공백뿐만아니라 뒤의 공백도 넣어줘야하는 특이한 조건의 문제로
    # 34번 줄을 보면 앞, 뒤에 모두 공백을 넣어준 것을 볼 수 있음
    result[i]=space+result[i]+space

for i in result:
    print(i)