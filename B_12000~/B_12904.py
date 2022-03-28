# reverse()와 sort(reverse=True)의 차이점을 알 필요가 있었다.
# reverse()는 배열 자체를 뒤집는 것이고
# sort(reverse=True)는 오름차순 정렬에서 내림차순으로 바꾸는 것이다.

# 입력값에서 A를 추가하거나, 뒤집고 B를 추가하는 것이 아니라
# 결과값에서 A를 제거하거나, B를 제거하고 뒤집는 사고방식이 필요했다.

import sys

S=list(map(str,sys.stdin.readline().rstrip('\n'))) # B
SLen=len(S)

T=list(map(str,sys.stdin.readline().rstrip('\n'))) # [A,B,B,A]

result=''.join(T) # ABBA

count=1

while ''.join(S)!=result: # S와 result를 비교
    if SLen > len(T): # S의 문자열 길이보다 T의 문자열 길이가 작으면 0을 반환 후 break
        count=0
        break
    elif T[-1]=='A': # 결과값의 마지막 문자열이 'A'이면 'A' 제거
        del T[-1]
    elif T[-1]=='B': # 결과값의 마지막 문자열이 'B'이면 'B' 제거 후 문자열 뒤집기
        del T[-1]
        T.reverse() # 문자열 뒤집기
    result=''.join(T)

print(count)