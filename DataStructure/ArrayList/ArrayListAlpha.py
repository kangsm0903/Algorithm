from LinkedList.MyList import MyList
import ctypes

class ArrayList(MyList):
    length=0

    def __init__(self):
        # 빈 array 생성
        self._n=0 # 실질적인 원소 개수 카운트
        self._capacity=1 # 배열 크기 
        self._A=self._make_array(self._capacity)

    def __len__(self):
        # 배열에 저장된 원소 갯수 반환
        return self._n

    def __getitem__(self,k):
        if 0<=k and k<self._n:
            return self._A[k]
        else:
            raise IndexError("invalid index")

    def append(self,obj):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1

    def _resize(self,c):
        # 배열 크기 c만큼 배열 리사이즈
        B=self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A=B
        self._capacity=c

    def _make_array(self,c):
        # 배열 크기 c의 새로운 array 반환
        return (c*ctypes.py_object)( )

# -----------------------------------------------------------------------------------

    def __init__(self,size):
        self.item=size*[None] #사이즈 만큼 배열 생성
        self.length=0
        self.size=size

    def len(self):
        return self.length

    def getitem(self,idx):
        if(self.length<=idx):
            raise IndexError ("idx out of bound")
        else:
            return self.item[idx]

    def setitem(self,idx,value):
        if(self.length<=idx):
            raise IndexError ("idx out of bound")
        else:
            self.item[idx]=value

    def insertItem(self, idx, value):

        if idx==self.length-1:
            self.item[idx]=value
            self.length+=1
        else:
            for i in range(self.length,idx+1,-1): # 삽입 시 idx부터 마지막 인덱스까지 한칸 씩 미룸
                self.item[i]=self.item[i-1]
            self.item[idx]=value

# -------------------------------------------------------------------------------------------------

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