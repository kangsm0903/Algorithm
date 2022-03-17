# 1~9까지 숫자를 할당하기 전에 각 알파벳의 자릿수를 계산해줌
# Ex. ACDEB 라면 A=10000, C=1000, D=100, E=10, B=1
# Ex.   GCF 라면                  G=100, C=10, F=1
# Ex. A=10000, C=1010, D=100, G=100, E=10, C=10, B=1, F=1
# 자릿수가 높은 순서대로 높은 숫자를 할당 9~1
# 각 자릿수를 더하기

import sys

N=int(sys.stdin.readline())

alphabet={'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
case=[]

count=0

for i in range(N):
    case.append(list(map(str,sys.stdin.readline().rstrip('\n')))) # ACDEB, GCF

for k in case:
    position_num=len(k) # 5
    for l in list(k):
        alphabet[l]+=10**(position_num-1)
        position_num-=1

for p in range(9,0,-1):
    count=count+max(alphabet.values())*p
    del alphabet[max(alphabet,key=alphabet.get)]

print(count)