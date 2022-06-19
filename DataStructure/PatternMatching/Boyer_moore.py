# character-jump 부분을 모르겠음

def find_boyer_moore(T,P): # T=주어진 문자열 [a,b,c,a,a,c]/ P=찾고자하는 단어 [a,a,c]
    n,m=len(T), len(P)

    if m==0: # 주어진 길이가 0이면 0을 반환하고 끝냄 
        return 0
    
    last={}
    for k in range(m):
        last[P[k]]=k

    # 리스트의 맨 마지막 원소에 접근하기 위해 -1을 해주는 것 같음 - 배열 인덱스는 0부터 시작이니까
    i=m-1 # i는 주어진 배열 기준
    k=m-1 # k는 찾고자하는 단어 기준

    while i<n:
        if T[i]==P[k]:  # 두 문자가 같다면
            if k==0:    # k==0인지 확인: 0이라면 주어진 단어와 모두 동일한 문자들을 찾았다는 뜻     
                return i# 따라서 주어진 단어가 시작되는 지점의 인덱스를 반환
            else:       # k!=0이라면 i-=1로 왼쪽으로 이동하여 다음 문자가 같은 지 탐색
                i-=1
                k-=1
        else:           # 두 문자가 다르다면 - Character-jump
            j=last.get(T[i],-1) # T[i]의 value값을 받아오는데 없다면 -1 디폴트값을 반환
            i+=m-min(k,j+1) 
            k=m-1
    return -1

a = find_boyer_moore(["a","b","c","a","a","c"],["a","a","c"])
print(a)