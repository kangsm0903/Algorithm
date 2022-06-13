import HashMapBase
from UnsortedTable import UnsortedTableMap

class ChainHashMap(HashMapBase):
    def _bucket_getitem(self,j,k):  # key=j / value=k
        bucket=self._table[j]       # 테이블에서 key=j를 bucket에 할당
        if bucket is None:          # bucket이 None이라면 에러 아니면 value값 반환
            raise KeyError("Key Error: "+repr(k))
        return bucket[k]

    def _bucket_setitem(self, j,k,v): 
        if self._table[j] is None:
            self._table[j]=UnsortedTableMap()
        oldsize=len(self._table[j]) # None이 아니면 길이 측정
        self._table[j][k]=v         # 값 갱신
        if len(self._table[j])>oldsize:
            self._n+=1              # 사이즈 업

    def _bucket_delitem(self,j,k):  # j로 해당 원소 접근
        bucket=self._table[j]
        if bucket is None:          # None이면 에러 아니면 삭제
            raise KeyError("Key Error: "+repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:  # table들을 bucket에 하나씩 넣고 
            if bucket is not None:  # None이 아니면 bucket의 key값들을 iterable한 형태로 반환
                for key in bucket:
                    yield key