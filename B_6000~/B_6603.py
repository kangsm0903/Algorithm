# N&M 풀이와 동일
# 오름차순
# 중복은 있을 수가 없고
# visited 필요

k=10

while True:
    if k==0:
        break
    case=list(map(int,input().split()))

    k=case[0]

    case=case[1:]
    case.sort() # 혹시 모를 오름차순 정렬

    visited=[0]*len(case)

    result=[]

    def is_promising():
        base=int(result[0])
        for i in range(1,len(result)):
            if base>int(result[i]):
                return False
            else:
                base=int(result[i])
        return True

    def BruteForce():
        if len(result)==6:
            print(' '.join(result))
            return
        
        for i in range(len(case)):
            if visited[i]==0: # 방문하지않았다면
                result.append(str(case[i]))
                visited[i]=1
                if is_promising():
                    BruteForce()
                result.pop()
                visited[i]=0

    BruteForce()
    print()