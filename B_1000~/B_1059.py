L = int(input()) # 8 

S = list(map(int, input().split())) 

n = int(input())

plus = []
minus = []

end = []

if min(S) > n:
    end.append(min(S)-n)
    end.append(n)
    print(end[1]*end[0]-1)
elif n in S:
    print(0)
else:
    for i in range(0,L):
        result = S[i]-n
        if result > 0:
            plus.append(result)
        else:
            minus.append(result)
            
    end.append(min(plus))
    end.append(abs(max(minus)))
    
    print(end[0]*end[1]-1)
