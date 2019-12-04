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
# n의 최대 약수가 sqrt(n) 이하이므로 j = n**0.5 까지 검사

# 소수 구하기
# 0. 구할 범위 지정
# 1. 2는 소수
# 2. 2를 제외한 2의 배수 제외
# 3. 3은 소수
# 4. 3을 제외한 3의 배수 제외
# 5. 5는 소수
# 6. 5를 제외한 5의 배수 제외
# 7. 7은 소수
# 8. 7을 제외한 7의 배수 제외
# 9. 남은 수가 소수