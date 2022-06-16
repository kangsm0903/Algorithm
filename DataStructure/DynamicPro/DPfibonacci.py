d=[0]*100 # 계산된 값을 저장할 배열 생성

def DPfibonacci(idx): # Dynamic Programming을 이용한 피보나치 수열
    '''
    idx가 1,2일 때는 1을 반환함으로 재귀의 멈춤 조건을 설정

    d[idx]!=0 일 때, d[idx]에 이미 계산된 값이 저장된 것이기에 그 값을 반환 
    d[idx]==0 일 때, d[idx]에 계산된 값을 저장 Memoization
    '''
    if idx==1: 
        return 1
    elif idx==2:
        return 1

    elif d[idx]!=0:
        return d[idx]
    else:
        d[idx]=DPfibonacci(idx-1)+DPfibonacci(idx-2)
        return d[idx]
    
print(DPfibonacci(30)) # 832040

def fibonacci(num): # 일반적인 재귀로 구현한 피보나치 수열
    if num==1:
        return 1
    elif num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)