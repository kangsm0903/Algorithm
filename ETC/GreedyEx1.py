'''
1. N이 K로 나누어 떨어진다면 N을 K로 나눈다.
2. 나누어 떨어지지않으면 N에서 1을 뺀다.

정당성 분석
가능하면 최대한 많이 나누는 작업이 최적의 해를 보장하는 이유
N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 줄어들기 때문이다
즉, K가 2이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 N을 빠르게 줄일 수 있다.
또한, N은 항상 1에 도달하게 된다.
'''

# 내 풀이
N,K=map(int,input().split())

count=0

while N!=1:
    if N%K==0:
        N=N//K
        count+=1
    else:
        N-=1
        count+=1

print(count)

# ------------------------------------------------------
'''
내 풀이의 while문은 한번 돌 때마다 K로 나뉠수도, 1로 뺄수도 있기에
아래의 풀이보다 속도가 느리다.

while문이 한번 실행될 때마다 무조건 K로 나누어지기 때문에
시간복잡도가 logN으로 줄어 큰 범위에서도 잘 돌아감
'''

N,K=map(int,input().split())

count=0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target=(N//K)*K 
    count+=(N-target) # 1을 밴 횟수를 count에 더함
    n=target          # n 갱신

    if N<K:           # N이 K보다 작다면 break
        break;
    
    # K로 나누는 연산 1번 시행하기에 count+=1
    count+=1
    N//=K

# 남은 수를 1로 뺀 횟수를 더해줌
count+=(n-1)
print(count)