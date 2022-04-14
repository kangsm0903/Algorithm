class ArrayList(object):
    # 배열 기반 리스트
    length=0
    def __init__(self,size):
        self.item=size*[None]
        self.length=0
        self.size=size

    def len(self):
        return self.length
    
    def is_empty(self):
        return self.length==0

    def get_item(self,idx): # 아이템 가져오기
        if self.is_empty(): # 빈 리스트면 에러 반환
            raise ValueError ("List is empty")
        return self.item[idx]


    def set_item(self,idx,data): # 값 바꾸기
        if self.is_empty():      # 빈 리스트면 에러 반환
            raise ValueError ("List is empty")
        elif self.length<=idx:   # 인덱스가 리스트 길이보다 클 때
            raise IndexError ("Index out of bound")
        self.item[idx]=data

    def insert_item(self, data, idx): # 삽입
        if self.length<idx:
            raise IndexError ("Index out of bound")
        for i in range(self.length,idx-1,-1):
            self.item[i+1]=self.item[i] # i번째 인덱스를 i+1로 이동
        self.item[idx]=data
        self.length+=1

    def remove_item(self,idx): # 삭제
        if self.is_empty():
            raise ValueError ("List is empty")
        elif self.length<=idx:
            raise IndexError ("Index out of bound")
        for i in range(idx+1,self.length):
            self.item[i-1]=self.item[i]
        self.length-=1
    
    def printMyList(self):
        for i in range(self.length):
            print(self.get_item(i),end=' ')
        print()

if __name__ == "__main__":
    List=ArrayList(10)
    List.insert_item("world",0)
    List.insert_item("hello",0)

    List.printMyList()

    List.remove_item(1)
    List.printMyList()