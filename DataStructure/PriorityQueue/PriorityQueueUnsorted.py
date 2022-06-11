# Unsorted list
# insert O(1)
# delete O(N)
class PriorityQueue(object):
    def __init__(self):
        self.queue=[]

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
        # self.queue의 원소들을 string으로 바꾸고 합침
    
    def isEmpty(self):
        return len(self.queue)==0

    def insert(self,data): # 맨 뒤에 data 삽입
        self.queue.append(data)

    def delete(self):
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