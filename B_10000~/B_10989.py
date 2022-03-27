# [0]으로 배열 10001개를 만들고 입력되는 숫자들의 갯수를 카운팅한다.
# 카운팅된 숫자만큼 인덱스번호를 반환한다.
import sys

N=int(sys.stdin.readline())

result = [0]*10001
count=0

for i in range(N):
    A=int(sys.stdin.readline())
    result[A]+=1

for i in result:
    for l in range(i):
        print(count)
    count+=1
