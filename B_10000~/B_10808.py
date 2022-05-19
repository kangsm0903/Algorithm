import sys

key="abcdefghikjlmnopqrstuvwxyz"

ls = [0 for i in range(26)] # [0,0,0,0,...]

S=sys.stdin.readline().strip() # baekjoon
for i in range(26):
    ls[i]=S.count(key[i]) # key[i] 문자열도 인덱싱으로 접근 가능

print(ls)

# ----------------------------------------------------------------------

x = sys.stdin.readline().strip() # baekjoon

abc = [0]*26

for i in x:
    abc[ord(i)-ord('a')] +=1 
    # ord(i) 해당 유니코드 정수를 반환 ord('a')==97
    # 따라서 [ord('a')-ord('a')]이면 abc[0] 인덱스 위치에 +1
    # [ord('b')-ord('a')]이면 98-97로 abc[1] 인덱스 위치에 +1

print(*abc)

# ----------------------------------------------------------------------

case=[0 for i in range(26)]

a = list(str(input()))

for i in a:
    if i=='a':
        case[0]+=1
    elif i=='b':
        case[1]+=1
    elif i=='c':
        case[2]+=1
    elif i=='d':
        case[3]+=1
    elif i=='e':
        case[4]+=1
    elif i=='f':
        case[5]+=1
    elif i=='g':
        case[6]+=1
    elif i=='h':
        case[7]+=1
    elif i=='i':
        case[8]+=1
    elif i=='j':
        case[9]+=1
    elif i=='k':
        case[10]+=1
    elif i=='l':
        case[11]+=1
    elif i=='m':
        case[12]+=1
    elif i=='n':
        case[13]+=1
    elif i=='o':
        case[14]+=1
    elif i=='p':
        case[15]+=1
    elif i=='q':
        case[16]+=1
    elif i=='r':
        case[17]+=1
    elif i=='s':
        case[18]+=1
    elif i=='t':
        case[19]+=1
    elif i=='u':
        case[20]+=1
    elif i=='v':
        case[21]+=1
    elif i=='w':
        case[22]+=1
    elif i=='x':
        case[23]+=1
    elif i=='y':
        case[24]+=1
    elif i=='z':
        case[25]+=1

print(*case)