from random import randrange
import MapBaseABC

class HashMapBase(MapBaseABC):
    def __init__(self, cap=11, p=109345121):
        self._table=cap*[None] # 11개의 배열 생성
        self._n=0
        self._prime=p # prime for MAD compression
        self._scale=1+randrange(p-1)
        self._shift=randrange(p)

    def _hash_function(self,k):
        return (hash(k)*self._scale+self._shift)%self._prime%len(self._table)

    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        j=self._hash_function(k)
        return self._bucket_getitem(j,k)

    def __setitem__(self,k,v):
        j=self._hash_function(k)
        self._bucket_function(j,k,v)
        if self._n>len(self._table)//2:
            self._resize(2*len(self._table)-1)
        
    def __delitem__(self,k):
        j=self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n-=1

    def resize(self,c):
        old=list(self.items())
        self._table=c*[None]
        self._n=0
        for (k,v) in old:
            self[k]=v