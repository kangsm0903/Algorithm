from random import randrange
from UnsortedTable import Mapbase

class HashMapBase(Mapbase):
    
    def __init__(self, cap=11, p=109345121):
        # prime, scale, shift는 뭔지 모르겠음
        self._table=cap*[None]  # 배열 11개 생성
        self._n=0               # 현재 배열의 입력된 값의 개수
        self._prime=p           # prime for MAD compression
        self._scale=1+randrange(p-1) 
        self._shift=randrange(p)

    def _hash_function(self,k): # 수문장으로서 고유의 key값을 반환해줌
        return (hash(k)*self._scale+self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self,k): # 해시함수로부터 key값을 받아서 key-value를 반환
        j=self._hash_function(k) # key값
        return self._bucket_getitem(j,k) # key-value

    def __setitem__(self, k,v): # 해시함수로부터 key값을 받아서 value값을 갱신
        j=self._hash_function(k)
        self._bucket_setitem(j,k,v)
        if self._n > len(self._table) // 2: # 입력값의 개수 > 테이블의 크기 일 때,
            self._resize(2*len(self._table)-1) # 테이블 크기의 2배로 resize 진행

    def __delitem__(self,k):    # 해시함수로부터 key값을 받아서 그걸 토대로 삭제
        j=self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n-=1              # 입력값의 개수를 하나 줄임

    def _resize(self,c):        
        old=list(self.items())  # item들을 리스트 형태로 old에 할당
        self._table=c*[None]    # table을 빈 리스트로 만들어줌
        self._n=0               # 입력값의 개수를 0으로 설정
        for (k,v) in old:       # item들이 들어있는 old를 새로 resize한 table에 넣어줌
            self._table[k]=v    
