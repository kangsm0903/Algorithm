from bintrees import BinaryTree
from bintrees import AVLTree

# 1번 이진 트리의 삽입 과정을 보이기
# 2번 이진 트리의 삭제 과정을 보이기
btree1=BinaryTree()

# 3번 AVL 트리의 삽입 과정을 보이기
# 4번 AVL 트리의 삭제 과정을 보이기
avltree1=AVLTree() 

# 1번 문제 (5,3,6,7,4,1,9) 삽입을 보이고 전위, 중위, 후위순회를 진행
btree1.insert(5,None)
btree1.insert(3,None)
btree1.insert(6,None)
btree1.insert(7,None)
btree1.insert(4,None)
btree1.insert(1,None)
btree1.insert(9,None)

# foreach(func, order) order - 0 in, +1 post, -1 pre
# key값만 출력하는 함수 
def test(k,v):
    print(k, end=' ')

print("1.")
print("In-order     ", end="")
btree1.foreach(test,0) # 0 : in-order
print()
print("Pre-order    ", end="")
btree1.foreach(test,-1) # -1 : pre-order
print()
print("Post-order   ", end="")
btree1.foreach(test,+1) # +1 : post-order
print()

# BinaryTree에서 1,3,5,7,9를 삭제하고 전위, 중위, 후위순회를 진행
btree1.remove(1)
btree1.remove(3)
btree1.remove(5)
btree1.remove(7)
btree1.remove(9)

print("2.")
print("In-order     ", end="")
btree1.foreach(test,0) # 0 : in-order
print()
print("Pre-order    ", end="")
btree1.foreach(test,-1) # -1 : pre-order
print()
print("Post-order   ", end="")
btree1.foreach(test,+1) # +1 : post-order
print()

# AVL Tree에 1,3,5,7,9 삽입 후 전위, 중위, 후위순회 진행
avltree1.insert(5,None)
avltree1.insert(3,None)
avltree1.insert(6,None)
avltree1.insert(7,None)
avltree1.insert(4,None)
avltree1.insert(1,None)
avltree1.insert(9,None)

print("3.")
print("In-order     ", end="")
avltree1.foreach(test,0) # 0 : in-order
print()
print("Pre-order    ", end="")
avltree1.foreach(test,-1) # -1 : pre-order
print()
print("Post-order   ", end="")
avltree1.foreach(test,+1) # +1 : post-order
print()

# AVL Tree에서 1,3,5,7,9 삭제 후 전위, 중위, 후위순회 진행
avltree1.remove(1)
avltree1.remove(3)
avltree1.remove(5)
avltree1.remove(7)
avltree1.remove(9)

print("4.")
print("In-order     ", end="")
avltree1.foreach(test,0) # 0 : in-order
print()
print("Pre-order    ", end="")
avltree1.foreach(test,-1) # -1 : pre-order
print()
print("Post-order   ", end="")
avltree1.foreach(test,+1) # +1 : post-order
print()