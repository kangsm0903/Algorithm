# 과제 4

from LinkedListBasedQueueADT import MyQueue

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node = next_node
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedListBasedQueue(MyQueue):

    def __init__(self, head=None, tail=None):
        self.head=None
        self.tail=None
        self.length=0

    def len(self):          # 길이 반환
        return self.length

    def first(self):        # head의 데이터값 반환
        if self.is_empty(): # 큐가 비어있으면 비어있다고 리턴
            return "Queue is empty"
        return self.head.data

    def is_empty(self):     # 비어있으면 True 아니면 False
        return self.head==None

    def enqueue(self, data): # 큐이기에 맨 뒤에 삽입
        new_node=Node(data)  # data를 가진 새 노드 생성

        if self.tail==None:  # tail==None이라면 head==tail==새 노드
            self.tail=new_node
            self.head=new_node
            self.length+=1
            return
        self.tail.next_node=new_node # tail 다음 노드를 새 노드로 설정
        self.tail=new_node           # 새 노드를 tail로 설정
        self.length+=1

    def dequeue(self, j=0):
        if self.is_empty():
            return "Queue is empty"
        node=self.head      # head를 node에 할당
        self.head=node.next_node # node의 다음 노드를 head로 설정 - 그 전의 노드는 사라짐
        self.length-=1

        if(self.head==None): # head가 비어있으면 tail도 비어있음 
            self.tail=None   # enqueue의 37번 줄을 위해 None을 할당함
            self.length=0

    def printMyList(self):
        node=self.head
        while node is not None:
            print(node.data, end=" ")
            node=node.next_node
        print()

q=LinkedListBasedQueue() # 큐 생성

q.enqueue(5)            # 5, 3 insert
q.enqueue(3)

q.printMyList()         # q 출력
print(q.len())          # q.length 출력

q.dequeue()             # item 2개 제거
q.dequeue()

print(q.is_empty())     # is_empty 확인

print(q.dequeue())      # item 제거 시도 결과

q.enqueue(7)            # 7, 9 insert
q.enqueue(9)

print(q.first())        # 첫 item 출력