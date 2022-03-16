# Node 클래스 정의
class Node:
    def __init__(self,data): # 생성자
        self.data=data
        self.next=None

# Linked List 클래스 정의
class LinkedList:
    # 초기화 메소드
    def __init__(self,data):
        self.head=None(data)

    # head부터 탐색하면서 뒤에 새로운 노드 추가
    def append(self, data):
        cur=self.head # cur=현재노드
        while cur.next is not None: # cur.next가 존재하면 cur=cur.next
            cur=cur.next
        cur.next=Node(data)
    
    def print_all(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next
        
    def get_node(self, index):
        cnt=0
        node=self.head
        while cnt<index: # cnt<index 라면 cnt+=1 하고 다음노드로 이동
            cnt+=1
            node=node.next
        return node
    
    # 삽입
    def add_node(self, index, value):
        new_node=Node(value)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            return
        node=self.get_node(index-1)
        next_node=node.next
        node.next=new_node
        new_node.next=next_node

    def delete_node(self, index):
        if index==0: # 첫 노드를 삭제할 것이라면 head.next 노드를 self.head로 설정하고 첫 노드는 삭제
            self.head=self.head.next
            return
        node=self.get_node(index-1) # 삭제하려는 노드의 전 노드를 node에 할당
        node.next=node.next.next # 전 노드의 next를 node의 다음 다음과 연결 
        # [5]->[6]->[12]->[8]

        # [5]->[12]->[8]  ----[6]----
        # 삭제하려는 [6]의 전 노드 [5]를 할당하고 [5]의 next.next와 연결
  