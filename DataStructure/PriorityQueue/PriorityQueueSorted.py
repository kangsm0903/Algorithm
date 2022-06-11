# Sorted list
# insert O(N)
# delete O(1)
class PriorityQueue(object):
    def __init__(self):
        self.queue=[]

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
        # self.queue의 원소들을 string으로 바꾸고 합침
    
    def isEmpty(self):
        return len(self.queue)==0

    def insert(self,data): # 순서대로 탐색 후 삽입
        if self.isEmpty(): # 큐가 비어있으면 그냥 삽입
            self.queue.append(data)
        else:              # 큐의 첫 원소가 data보다 크면 첫번째 인덱스에 data 삽입
            if self.queue[0]>data:
                self.queue.insert(0,data)
            else:          
                for i in range(len(self.queue)):
                    # self.queue[i]<data이고 다음 인덱스가 None일 경우 맨 뒤에 삽입
                    if self.queue[i]<=data and len(self.queue)==i+1:
                        self.queue.append(data)
                        break
                    # self.queue[i]<data<self.queue[i+1]일 때 i+1에 삽입
                    elif self.queue[i]<=data and self.queue[i+1]>=data:
                        self.queue.insert(i+1,data)
                        break

    def delete(self): # 맨 앞 삭제
        item = self.queue[0]
        del self.queue[0]
        return item

if __name__=='__main__':
    myQueue=PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7) # myQueue=[1,7,12,14]
    print(myQueue)
    myQueue.delete() # 최솟값 1 삭제
    print(myQueue)
    myQueue.delete() # 그 다음 최솟값 7 삭제
    print(myQueue)