'''
각 자리가 0~9로 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 +, *를 넣어 
만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
(0+2)*9)*8)*7)*5 이런 식

target의 첫번째 원소가 0,1일 경우 무조건 더해주는 것이 더 크기에 이 경우와
그 다음으로 있는 원소가 0,1일 경우 더해주는 경우만을 고려해준다.
'''
data=input()

result=int(data[0]) # 문자열의 첫번째 인덱스 값을 할당

for i in range(1, len(data)):
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)