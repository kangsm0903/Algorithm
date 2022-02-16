N,M=input().split()
M=int(M)
P=[]
m=[]

for i in range(int(N)): # 입력값들 P,m에 넣어놓음
    P.append(list(map(int,input().split())))
    m.append(sorted(list(map(int,input().split()))))

malig=[] # P[i][0] 신청인원 P[i][1] 수강인원 
for i in range(int(N)):
    if P[i][0]<P[i][1]: # 신청인원 < 수강인원일때 마일리지 최솟값 1
        malig.append(1)
    elif P[i][0]==P[i][1]: # 신청인원 = 수강인원일때 리스트의 최솟값
        malig.append(m[i][0])
    else: # 신청인원 > 수강인원일때 신청과 수강의 차이만큼의 리스트 인덱스값
        malig.append(m[i][P[i][0]-P[i][1]])

count=0
malig.sort() # 마일리지값들 정렬
for i in malig:
    if M-i<0: # 총 마일리지에서 리스트의 마일리지값을 최솟값부터 뺌
        break
    else:
        M-=i
        count+=1

print(count)