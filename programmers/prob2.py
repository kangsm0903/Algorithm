def solution(n):
    
    b = []
    
    for i in range(len(str(n))-1,-1,-1):
        b.append(n // 10**i)
        n = n % 10**i
        
    b.sort(reverse=True)
    
    c = str(b[0]) + str(b[1])
                   
    for i in range(2, len(b)):
        c = str(c) + str(b[i])
                   
    answer = int(c)
    return answer