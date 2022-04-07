# 과제 2

from MyList import MyList
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self): # 데이터 반환
        return self.data

    def set_data(self, data): # 데이터 삽입
        self.data=data

    def get_next(self):                 # 다음 노드로 이동
        return self.next_node

    def set_next(self,new_next):        # 다음 노드를 새 노드로
        self.next_node=new_next

class LinkedList(MyList):

    def __init__(self,head=None):
        self.head=None
        self.length=0

    def len(self):
        return self.length

    def getitem(self, j):               # j 번째 인덱스 노드 반환
        count=0
        node=self.head
        while count<j:                 # j 직전까지 계속 while 돌리면서 get_next(), 마지막에 node.get_data()
            count+=1
            node=node.next_node
        return node

    def setitem(self, val, j):          # j번째에 val 넣기
        count=0
        node=self.head
        while count<j:
            count+=1
            node.next_node
        node.set_data(val)

    def insertItem(self, item, j=0):    # A -> B -> D 에서 B와 D사이에 C 삽입 j=2
        new_node=Node(item,None)        # C
        if j==0:
            new_node.next_node=self.head
            self.head=new_node
            self.length+=1
            return
        node=self.getitem(j-1)          # self.getitem(1) == B
        nextNode=node.next_node         # node.next_node == D
        node.next_node=new_node         # B의 다음 노드를 C로 설정
        new_node.next_node=nextNode     # C의 다음 노드를 D로 설정
        self.length+=1

    def removeItem(self, j=0):          # A -> B -> C -> D 에서 C를 삭제하고 싶음
        if (j==0):                      # 만약 j==0이라면
            self.head=self.head.next_node     # head의 다음 노드를 head로 설정
            self.length-=1
            return
        else:
            preNode=self.getitem(j-1)       # node = B
            preNode.next_node=preNode.next_node.next_node
            self.length-=1

    def printMyList(self):
        node=self.head
        while node is not None:
            print(node.data, end=' ')
            node=node.next_node
        print()

S=LinkedList()
S.insertItem('4',0) # '4','3','1'을 position 0에 insert
S.insertItem('3',0)
S.insertItem('1',0) 

S.insertItem('2',1) # '2'를 position 1에 insert

S.printMyList() # 출력 1 2 3 4

S.removeItem(3) # position 3 제거
S.removeItem(1) # position 1 제거
S.removeItem(0) # position 0 제거

S.printMyList()