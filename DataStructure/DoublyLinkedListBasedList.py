# 과제 3

from MyList import MyList

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data=data                  # 현재 데이터
        self.next_node=next_node        # 다음 데이터
        self.prev_node=prev_node    # 이전 데이터

    def get_data(self):                 # 데이터 반환
        return self.data
    
    def set_data(self, data):           # 데이터 갱신
        self.data=data

    def get_next(self):                 # 다음 노드 반환
        return self.next_node

    def set_next(self, new_next):       # 다음 노드를 new_next로 할당
        self.next_node=new_next

    def get_previous(self):             # 이전 데이터 반환
        return self.prev_node

    def set_previous(self, new_next):   # 이전 노드 갱신
        self.prev_node=new_next

class DoublyLinkedList(MyList):
    
    def __init__(self):
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

    def insert(self, data, j):
        new_node=Node(data,None,None)
        if self.head==None:
            self.head=new_node
            self.length+=1
        elif j==0: # 맨 앞일 때
            self.head.prev_node=new_node
            new_node.next_node=self.head # new_node -> self.head
            self.head=new_node           # self.head 갱신
            self.length+=1
        elif j==(self.length): # 마지막에 삽입일 때
            node=self.getitem(j-1)
            node.next_node=new_node
            new_node.prev_node=node
            self.length+=1
        else: # 그 외의 경우 - 중간에 넣을 때 A->C->D
            node=self.getitem(j-1) # node=A
            node2=self.getitem(j)# node=C
            new_node.next_node=node2 # B->C
            new_node.prev_node=node
            node.next_node=new_node # A->B
            node2.prev_node=new_node
            self.length+=1
        
    def remove(self, j):
        if self.head==None:
            raise ValueError ('List is empty')
        elif j>self.length:
            raise IndexError ('Index out of bound')
        elif j==0:# 맨 앞일 때
            self.head=self.head.next_node
            self.head.prev_node=None
            self.length-=1
        elif j==(self.length-1): # 마지막일 때
            node=self.getitem(j-1)
            node.next_node=None
            self.length-=1
        else:
            node=self.getitem(j-1) # A->B->C node=A
            node.next_node=node.next_node.next_node # A->C
            node.next_node.prev_node=node # A<-C
            self.length-=1

    def printMyList(self):
        node=self.head
        while node is not None:
            print(node.data, end=' ')
            node=node.next_node
        print()

L=DoublyLinkedList()

L.insert('4',0) # position 0에 4,3,1 insert
L.insert('3',0)
L.insert('1',0)

L.insert('2',1) # position 1에 2 insert

L.printMyList() # 출력

L.remove(3)     # position 3, 1, 0 제거
L.remove(1)
L.remove(0)
L.printMyList() # 출력