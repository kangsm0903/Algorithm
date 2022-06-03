class Node:
    def __init__(self,val):
        self.val=val
        self.leftChild=None
        self.rightChild=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def setRoot(self,val):
        '''
        입력 받은 val값을 Node로 생성하여 root로 설정
        '''
        self.root=Node(val)

    def find(self,val):
        '''
        root 노드가 존재하면 True, 아니면 False
        '''
        if(self.findNode(self.root, val) is False):
            return False
        else:
            return True

    def findNode(self, currentNode, val):
        '''
        currentNode is None : 마지막 노드에 도달하여 None일 때
        val==currentNode.val: value return
        val <currentNode.val: leftChild에서 다시 findNode
        val >currentNode.val: rightChild에서 다시 findNode
        '''
        if(currentNode is None):
            return False # 찾으려는 노드가 없을 때
        elif (val==currentNode.val):
            return currentNode
        elif (val < currentNode.val): # 왼쪽으로
            return self.findNode(currentNode.leftChild,val)
        else:
            return self.findNode(currentNode.rightChild,val)

    def insert(self,val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        '''
        val<=currentNode.val: 왼쪽 서브트리
            currentNode.leftChild==True:leftChild가 존재하면 다시 재귀로 접근
            currentNode.leftChild==False:leftChild가 존재하지 않으면 Node(val)삽입

        val>currentNode.val: 오른쪽 서브트리
            currentNode.rightChild==True:rightChild가 존재하면 다시 재귀로 접근
            currentNode.rightChild==False:rightChild가 존재하지 않으면 Node(val)삽입
        '''
        if(val<=currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild,val)
            else:
                currentNode.leftChild = Node(val)
        elif(val>currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild,val)
            else:
                currentNode.rightChild=Node(val)

    def traverse(self):
        return self.traverseNode(self.root)

    def traverseNode(self, currentNode):
        '''
        중위 순회
        currentNode.leftChild is not None: 왼쪽 서브트리가 None이 아니면 결과에 traverseNode(leftChild) 추가
        currentNode is not None: 현재 노드가 None이 아니면 결과에 노드의 값 추가
        currentNode.rightChild is not None: 오른쪽 서브트리가 None이 아니면 결과에 traverseNode(rightChild) 추가
        '''
        result=[]
        if(currentNode.leftChild is not None):
            result.extend(self.traverseNode(currentNode.leftChild))
        if(currentNode is not None):
            result.extend([currentNode.val])
        if(currentNode.rightChild is not None):
            result.extend(self.traverseNode(currentNode.rightChild))
        return result