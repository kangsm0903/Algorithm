# Sorted list
# insert O(N)
# delete O(1)
class PriorityQueueBase:
    class _Item:
        __slots__='_key','_value'

    def __init__(self,k,v):
        self._key=k
        self._value=v

    def __It__(self,other):
        return self._key<other._key

class PriorityQueue(object):
    class _Item:
        __slots__='key','value'

    def __init__(self, k, v):
        self.key=k
        self.value=v
    
    def isEmpty(self):
        return len(self.queue)==0

    def insert(self,key,value): # Searching 후 data 삽입
        new=self.item(key,value)
        for i in range(len(self.queue)):
            self.queue.append(data)

    def delete(self): # 정렬되어 있기에 맨 앞의 원소를 삭제
        if self.isEmpty():
            raise ValueError ("Priority queue is empty")
        item=self.queue[0]
        del self.queue[0]

        try:
            min=0
            for i in range(len(self.queue)):
                if self.queue[i]<self.queue[min]: 
                    min=i # min 인덱스보다 작은 값이 나오면 min 갱신
            item=self.queue[i]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

if __name__=='__main__':
    myQueue=PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7) # myQueue=[12,1,14,7]
    print(myQueue)
    myQueue.delete() # 최솟값 1 삭제
    print(myQueue)
    myQueue.delete() # 그 다음 최솟값 7 삭제
    print(myQueue)