import BinarySearchTree

#Breadth First Search on Binary Search Tree

BFS=[]
def BSTBFS(curNode, i=0):
    if curNode==None:
        return
    BFS.append([])
    BFS[i].append(curNode.key)
    BSTBFS(curNode.leftChild, i+1)
    BSTBFS(curNode.rightChild, i+1)
    return BFS
