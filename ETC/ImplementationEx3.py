# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인함
# 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의한다.

# 내 풀이 - 그냥 씹 노가다
# ascii(a)==97 ~ ascii(h)==104

T=list(input()) # T=[a,1]

move=[-2,2] # 상 하 좌 우

cnt=0

if int(T[1])-2>=1: # 위로 2칸 움직였을 때, 
    if ord(T[0])+1<=104: # 오른쪽 1칸 움직였을 때, 104이내면 +1
        cnt+=1
    if ord(T[0])-1>=97: # 왼쪽 1칸 움직였을 때, 97 이상이면 +1
        cnt+=1

if int(T[1])+2<=8: # 아래로 2칸 움직였을 때,
    if ord(T[0])+1<=104:
        cnt+=1
    if ord(T[0])-1>=97:
        cnt+=1

if ord(T[0])+2<=104: # 오른쪽으로 2칸 움직였을 때,
    if int(T[1])-1>=1: 
        cnt+=1
    if int(T[1])+1<=8:
        cnt+=1

if ord(T[0])-2>=97: # 왼쪽으로 2칸 움직였을 때,
    if int(T[1])-1>=1:
        cnt+=1
    if int(T[1])+1<=8:
        cnt+=1

print(cnt)

# ------------------------------------------------------------------------------

input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0])) - int(ord('a')) + 1

steps=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

result=0

for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)