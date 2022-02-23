# 가능한 정답이 여러 가지인 경우 ex) 10,11,12,13,14,15,16,17,18 입력일 때 (10,16)(11,15)(12,14)...
# result=N 할당: 같은 객체를 참조하기에 무엇이든 동일하게 변경됨
# reuslt=N.copy() 값은 같아도 별개의 객체 서로 독립적임
N=[]

for i in range(9):
    N.append(int(input())) # N=[20,7,23,19,10,15,25,8,13]

result=N.copy()
remain=sum(N)-100 # 40

for i in range(len(N)): # 0~8
    if remain==N[i]*2 and result.count(N[i])==1:
        pass
    elif remain==N[i]*2 and result.count(N[i])>1:
        result.remove(N[i])
    elif remain-N[i] in N:
        result.remove(remain-N[i])
        result.remove(N[i])
        break
    else:
        pass

result.sort()
for k in result:
    print(k)