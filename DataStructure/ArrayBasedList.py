# 과제 1

from MyList import MyList

class ArrayBasedList(MyList):
    length=0

    def __init__(self, size):
        self.item = size*[None] # [][][] 배열 생성
        self.length=0
        self.size=size # 10

    def len(self):
        return self.length

    def getitem(self, j):
        if (self.length>j):
            return self.item[j]
        raise ValueError('value not in list')

    def setitem(self, val, j):
        if (self.length>j):  # 파이썬 인덱스는 0부터 시작이니까 마지막 인덱스를 6이라 한다면 self.length=7로 
            self.item[j]=val # self.length<j라면 오류를 리턴하는게 맞음
            return
        raise ValueError('index is out of bound')

    # full일 때 resize해야되는지 의문 -----
    def insertItem(self, item, j=0):
        if (self.length>=self.size): # length가 size를 넘었을 때
            raise ValueError('array is full')
        if (j<0): # j가 음수라면 self.length+j로 양수 인덱스로 변환
            j=self.length+j
        if (j>=self.size): # j가 self.length보다 크거나 같으면 인덱스 범위 초과 오류 출력
            raise ValueError("index out of bound")
        else: # self.length<self.size
            for i in range(self.length,j,-1):
                self.item[i]=self.item[i-1]
            self.item[j]=item
            self.length+=1

    def removeItem(self,j=0): # j번째 인덱스 삭제
        if (self.length>j):
            for i in range(j, self.length):
                self.item[i]=self.item[i+1]
            self.length-=1    # 길이 1 빼기
        else:
            raise ValueError('index is out of bound')

    def printMyList(self):
        for i in range(self.length):
            print(self.item[i], end=' ')
        print()

A=ArrayBasedList(10)
A.insertItem('4',0)
A.insertItem('3',0)
A.insertItem('1',0) # 4,3,1을 position 0에 insert

A.insertItem('2',1) # 2를 position 1에 insert

A.printMyList()     # list 출력

A.removeItem(3)     # position 3을 삭제
A.removeItem(1)     # position 1을 삭제
A.removeItem(0)     # position 0을 삭제

A.printMyList()     # list 출력
