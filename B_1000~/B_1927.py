# heap 최소힙을 이용했음 시간복잡도 O(log n)
import sys
import heapq
N=int(sys.stdin.readline())

heap=[]
Z=[]

for i in range(N):
    B=int(sys.stdin.readline())
    if len(heap)==0 and B==0:
        Z.append(0)
    elif B==0:
        Z.append(heapq.heappop(heap))
    else: # 자연수일때
        heapq.heappush(heap,B)

for i in Z:
    print(i)