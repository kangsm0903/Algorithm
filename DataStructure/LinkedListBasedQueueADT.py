from abc import ABCMeta, abstractmethod

class MyQueue(object):
    __metaclass__=ABCMeta

    def len(self): 
        # return the number of elements stored
        pass

    def first(self): 
        # returns the element at the front without removing it
        pass

    def is_empty(self):
         # return whether no elements are stored
        pass
    
    def enqueue(self, item):
        # add an item into the queue
        pass
 
    def dequeue(self): 
        # remove an item from the queue
        pass

    def printMyQueue(self): 
        # print the item in the queue
        pass