def solution(n):
    
    a = []
    
    for num in range(2,n+1): # 2~n까지
        remain = 0
        for i in range(1,n+1): # 1~n까지 나눴을때 나머지 0인게 2개여야함
            if num % i == 0:
                remain += 1
        if remain == 2:
            a.append(num)
    
    answer = len(a)
    return answer
 
# 소수니까 x를 1~9로 나누었을 때 나머지가 2개가 나와야함 (1과 x로써)
# remain이 나머지로 remain == 2일때 a 배열에 추가

# def is_prime(n):
#     return all([ (n%j) for j in range(2, int(n**0.5)+1)]) and n>1

# print(is_prime(10))