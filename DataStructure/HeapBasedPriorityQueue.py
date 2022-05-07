class HeapPriorityQueue(object):

    def parent(self,j): # 부모
        return (j-1)//2

    def left(self,j): # 왼쪽 데이터 인덱스 값 반환
        return 2*j+1

    def right(self,j): # 오른쪽 데이터 인덱스 값 반환
        return 2*j+2

    def has_left(self,j): # 데이터 길이보다 인덱스 값이 작으면 왼쪽에 데이터 있는 것
        return self.left(j) < len(self.data) 

    def has_right(self,j):
        return self.right(j) < len(self.data)

    def swap(self,i,j): # data[i]와 data[j]를 서로 바꿈
        self.data[i],self.data[j]=self.data[j],self.data[i]

    def upheap(self,j):
        parent=self.parent(j) # j의 부모
        if j>0 and self.data[j]<self.data[parent]: # j가 root가 아니고 (j>0) 부모보다 작을 때
            self.swap(j,parent) # 부모와 j를 swap
            self.upheap(parent) # swap 후 그 부모를 다시 upheap 검사를 함

    def downheap(self,j):
        # 처음에 자식 노드 둘 중 누가 더 작은 지 확인
        if self.has_left(j): # 왼쪽 값이 존재하면
            left=self.left(j) # 왼쪽 값 인덱스 반환
        if self.has_right(j): # 오른쪽 값이 존재
            right=self.right(j) # 오른쪽 값 인덱스 반환
        if self.data[left][0]<self.data[right][0]:
            small_child=left
        else:
            small_child=right
        # 왼쪽 오른쪽 중 누가 더 작은 지 확인됐다면 swap할려는 값과 비교
        if self.data[j][0]>self.data[small_child][0]:
            self.swap(j,small_child) # j와 small_child가 데이터값이 아니라 인덱스 값이기에 데이터만 swap
            self.downheap(small_child) # small_child 인덱스 값으로 재귀

    def __init__(self):
        self.data=[] # 배열

    def length(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def add(self, key, value):
        # key와 value 쌍을 삽입
        self.data.append((key,value)) # key,value를 튜플로 묶어 append
        self.upheap(len(self.data)-1) # len(self.data)-1 은 마지막 노드의 깊이(최대 깊이)
        # 최대 깊이부터 heap-order를 위해 upheap을 통해 정렬

    def return_min(self):
        if self.is_empty():
            raise ValueError("Priority Queue is empty")
        item=self.data[0] # (key,value)
        return (item[0], item[1]) # key값 value값 리턴

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority Queue is empty")
        self.swap(0,len(self.data)-1) # root와 last node swap
        item=self.data.pop() # 배열의 pop(공백)은 맨 마지막 값을 반환함 -> 전 root 반환
        self.downheap(0)
        return (item[0], item[1])

    def printMyList(self):
        for i in range(len(self.data)):
            print(self.data[i], end=' ')
        print()

if __name__ == '__main__':
    H=HeapPriorityQueue();
    H.add(3,12)  
    H.printMyList()
    H.add(6,1)
    H.printMyList()
    H.add(15,1)
    H.printMyList()
    H.add(12,30)  
    H.printMyList()
    H.add(2,20)
    H.printMyList()
    H.remove_min()
    H.printMyList()
    print(H.return_min())
    
    # upheap과 downheap을 할 때 swap할 노드 2개만 다루기에 
    # up,downheap을 거쳐간 노드를 제외하면 순서가 뒤죽박죽인 것이였음 - heap정렬이 root빼고 뒤죽박죽인 이유