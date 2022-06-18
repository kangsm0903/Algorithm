def merge_sort(S):
    n=len(S)
    if n<2:     # 계속 분할하면서 길이가 2가 되면 반환
        return
    mid=n//2    # 가운데 인덱스를 찾음 
    S1=S[0:mid] # 가운데를 기준으로 앞 부분
    S2=S[mid:n] # 가운데를 기준으로 뒷 부분

    merge_sort(S1)  # 재귀적으로 S1 다시 분할
    merge_sort(S2)  # 재귀적으로 S2 다시 분할
    merge(S1,S2,S)  # 길이가 최소 2로 분할한 것을 병합시작

def merge(S1,S2,S): # S1 + S2 = S
    i=j=0
    while i+j<len(S):
        if j==len(S2) or (i<len(S1) and S1[i] < S2[j]):
            S[i+j]=S1[i]
            i+=1
        else:
            S[i+j]=S2[j]
            j+=1