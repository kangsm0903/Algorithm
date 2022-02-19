import sys

K=int(sys.stdin.readline()) # 6

combine=[2**i for i in range(21)] # combine=[1,2,4,8,16,32,64..]
# 1 ≤ K ≤ 1,000,000이기에 combine에 2의20승까지 넣어줌
for i in combine:
    if K==i: # K가 2의 제곱 수 일때
        count=0
        break
    elif K<i: # K가 2의 제곱 수가 아닐 때는 K보다 큰 가장 가까운 제곱 수를 A에 할당함
        A=i # 8
        count=1
        tan=A//2
        break

if count==0:# K가 2의 제곱 수 일때
    print(K,0)
elif K%2==1: # K가 홀수일때
    print(A,combine.index(A))
else: # K가 짝수일때
    for l in range(combine.index(A)): # 짝수일때 최대로 분할 할 수 있는 경우가 제곱 수만큼이기에 combine.index(A)만큼 반복함
        if K!=tan and K>tan: # K와 tan이 다르고 K>tan 일때
            K=K-tan
            tan//=2
            count+=1
        elif K!=tan and K<tan: # K와 tan이 다르고 K<tan 일때
            tan//=2
            count+=1 
        else: # K와 tan이 같으면 멈추고 출력
            break    
    print(A,count)
