N,r,c=map(int,input().split()) # 배열의 크기, 행(가로), 열(세로)

def recursive(N,r,c):
    if N==0:
        return 0
    half=(2**N)//2 # 반지름

    if r<half and c<half: # 1사분면
        return recursive(N-1,r,c)
    elif r<half and c>=half: # 2사분면
        return half*half+recursive(N-1,r,c-half)
    elif r>=half and c<half: # 3사분면
        return 2*half*half+recursive(N-1,r-half,c)
    elif r>=half and c>=half: # 4사분면
        return 3*half*half+recursive(N-1,r-half,c-half)

print(recursive(N,r,c))