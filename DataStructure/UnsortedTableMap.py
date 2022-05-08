# Map (key,value) get, set, del method
import MapBaseABC

class UnsortedTableMap(MapBaseABC):
    def __init__(self):
        self._table=[]

    def __getitem__(self,k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: '+repr(k))

    def __setitem__(self,k,v):
        for item in self._table:
            if k==item._key:
                item.value=v
                return
        self._table.append(self._item(k,v)) # key값을 찾지 못한다면

    def __delitem__(self,k):
        for j in range(len(self._table)):
            if k==self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: "+ repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self): # iterable로 만듬
        for item in self._table:
            yield item._key