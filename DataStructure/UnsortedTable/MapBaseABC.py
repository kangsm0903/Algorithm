# MapBase Abstract Class

from typing import MutableMapping

class MapBase(MutableMapping):

    class _Item:
        __slots__='_keys','_value'

    def __init(self,k,v):
        self._key=k
        self._value=v
    
    def __eq__(self, other): # 같은 지 확인하는 메소드 같음
        return self._key == other.key

    def __ne__(self, other): # eq와 반대
        return not (self==other)

    def __It__(self,other): # key를 비교
        return self._key < other._key 