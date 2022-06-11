# Map (key,value) get, set, del method
import MapBaseABC

class UnsortedTableMap(MapBaseABC):
    def __init__(self):
        self._table=[1,2,3,4,5,6,7,8]

    def __getitem__(self,k):
        for item in self._table: # table의 원소들을 item(key,value)에 넣음
            if k == item._key: # item의 key가 주어진 k와 같다면
                return item._value # item의 value를 반환
        raise KeyError('Key Error: '+repr(k))

    def __setitem__(self,k,v):
        for item in self._table:
            if k==item._key: # 주어진 k에 맞는 item.key를 찾으면
                item.value=v # v로 value 갱신
                return
        self._table.append(self._item(k,v)) # key값을 찾지 못한다면

    def __delitem__(self,k):
        for j in range(len(self._table)):
            if k==self._table[j]._key: # table의 모든 원소들을 방문해서 key값 비교
                self._table.pop(j) # 값을 찾으면 pop
                return
        raise KeyError("Key Error: "+ repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self): # iterable로 만듬
        for item in self._table:
            yield item._key

a = UnsortedTableMap()

print(a.__getitem__(3))