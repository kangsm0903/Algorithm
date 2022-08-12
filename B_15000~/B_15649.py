# 1~N까지의 자연수 중 중복없이 M개를 고른 수열

N,M=map(int,input().split())

visited=[0]*(N+1)   # 방문여부를 확인 - idx[0]은 쓰지 않음
result=[0]*M        # M개의 원소를 담을 리스트

def BackTrack(idx):
    if idx==M:
        print(' '.join(result))
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=1 # 방문체크
            result[idx]=str(i)
            BackTrack(idx+1)
            visited[i]=0 # 방문체크 해제

BackTrack(0)