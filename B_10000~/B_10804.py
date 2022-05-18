case=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

test=[]

for i in range(10):
    test.append(list(map(int,input().split())))
    # test=[[5,10],[9,13],[1,2],[3,4],[5,6],[1,2],[3,4],[5,6],[1,20],[1,20]]

for i in test: #[5,10]
    last=i[1]-1 # 10
    for k in range(i[0]-1,((i[1]+i[0])//2)):
        a=case[last] # a=case[10] 10번째 값을 a에 저장
        case[last]=case[k] # case[10]=case[5] index 10 <-> index 5
        case[k]=a # case[5] = a
        last-=1

print(*case)

#-----------------------------------------------------------------------

card = [i for i in range(21)] # [0~20]

for _ in range(10):
  a, b = map(int, input().split())
  for i in range((b-a+1)//2): # 0부터 (b-a+1)//2까지 하나씩 증가하면서
    card[b-i], card[a+i] = card[a+i], card[b-i] # 양 끝을 swap 해줌

del card[0] # 처음 0 삭제
print(*card)