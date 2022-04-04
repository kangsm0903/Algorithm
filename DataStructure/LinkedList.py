class SList:
    
    class Node:
        def __init__(self, item, link): # 노드 생성자
            self.item=item # element
            self.next=link # 다음 노드 레퍼런스

    def __init__(self): # 단순 연결 리스트 생성자
        self.head=None
        self.size=0

    def size(self): # 노드 사이즈 반환
        return self.size

    def is_empty(self): 
        return self.size==0

    def insert_front(self,item): # 맨 앞에 삽입
        if self.is_empty(): # 비어있다면 새 노드를 head로 지정
            self.head=self.Node(item,None)
        else: # 새 노드가 head의 레퍼런스를 가리키고 이 노드를 head로 지정
            self.head=self.Node(item,self.head)
        self.size+=1

    def insert_after(self,item,p): # p 다음에 삽입
        p.next=self.Node(item,p.next) # 새 노드를 만들고 p.next 레퍼런스를 가리키고 이 노드를 p의 다음으로 설정
        self.size+=1

    def delete_front(self): # 맨 앞 삭제
        if self.is_empty(): # 비어있다면 에러 출력
            raise EmptyError('Underflow')
        else: # 맨 앞 다음의 노드를 head로 지정
            self.head=self.head.next
            self.size-=1
        
    def delete_after(self,p): # p 다음 노드 삭제
        if self.is_empty(): # 비어있다면 에러 출력
            raise EmptyError('Underflow')
        t=p.next # t에 p.next 레퍼런스를 할당
        p.next=t.next # p.next.next 레퍼런스를 p.next에 할당 
        # A -> B -> C 일 때 p.next = B를 p.next.next = C 로 할당해서 B를 삭제한 것
        self.size+=1

    def search(self,target):
        p=self.head
        for i in range(self.size):
            if target==p.item:
                return i
            p=p.next
        return None # 탐색 실패

    def print_list(self):
        p=self.head
        while p:
            if p.next != None:
                print(p.item, "->", end="")
            else:
                print(p.item)
        p=p.next # 노드들을 순차탐색

class EmptyError(Exception): # 에러처리
    pass

# ------------------------------------------------------------------------------------------

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
        new_node=Node(value) # 새 노드
        if index==0:
            new_node.next=self.head
            self.head=new_node
            return
        node=self.get_node(index-1) # B
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