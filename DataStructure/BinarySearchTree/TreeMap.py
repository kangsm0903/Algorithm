from UnsortedTable import Mapbase

class TreeMap(LinkedBinaryTree, Mapbase):
    def key(self):
        return self.element()._key

    def value(self):
        return self.element()._value

    def _subtree_search(self,p,k):
        if k==p.key():  # 주어진 key를 찾으면 반환
            return p
        elif k<p.key(): # 주어진 k가 p.key()보다 작으면 왼쪽으로 감
            if self.left(p) is not None: # self.left(p)가 비어있지않으면 그제야 왼쪽으로 감
                return self._subtree_search(self.left(p),k)
        else:
            if self.right(p) is not None:# self.right(p)가 비어있지않으면 그제야 오른쪽으로 감
                return self._subtree_Search(self.right(p),k)
        return p

    def _subtree_first_position(self,p):
        # Return Position of first item in subtree rooted at p
        # 서브트리의 루트인 p의 첫번째 원소의 위치를 반환
        walk=p
        while self.left(walk) is not None:
            walk=self.left(walk)
        return walk

    def _subtree_last_position(self,p):
        # Return Position of first item in subtree rooted at p
        # 서브트리의 루트인 p의 마지막 원소의 위치를 반환
        walk = p
        while self.right(walk) is not None:
            walk=self.right(walk)
        return walk

    def __getitem__(self,k):
        if self.is_empty(): # 비어있으면 에러반환
            raise KeyError('Key Error: '+repr(k))
        else:
            p=self._subtree_search(self.root(),k) # 루트부터 탐색 시작
            self._rebalance_access(p)
            if k != p.key(): # 못찾으면 에러 반환
                raise KeyError('Key Error: '+repr(k))
            return p.value()

    def __setitem__(self,k,v):
        if self.is_empty(): # self가 다 비어있으면
            leaf = self._add_root(self._Item(k,v)) # root이자 leaf노드인 새로운 노드 추가
        else:               # 비어있지 않으면 
            p=self._subtree_search(self.root(),k) # 탐색 시작
            if p.key()==k:  # key를 찾으면
                p.element()._value=v # 원소의 value를 갱신
                self._rebalance_access(p)
                return
            else:           # 못 찾으면
                item=self._Item(k,v) # item으로 새로 만듬
                if p.key()<k: # 기준치보다 크기에 오른쪽에 넣어줌
                    leaf=self._add_right(p,item)
                else:         # 기준치보다 작기에 왼쪽에 넣어줌
                    leaf=self._add_left(p,item)
            self._rebalance_insert(leaf)

    def __iter__(self):
        p=self.first()
        while p is not None:
            yield p.key()
            p=self.after(p)

    def delete(self,p): # 노드 삭제
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element()) # p와 replacement.element를 교체
            p=replacement
        parent=self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty(): # 비어있지않다면
            p=self._subtree_search(self.root(),k) # 루트부터 탐색 시작
            if k==p.key():
                self.delete(p) # p노드 삭제
                return
            self._rebalance_access(p)
        raise KeyError("Key Error: "+repr(k))
