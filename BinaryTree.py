class Node():
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.leftChild=None
        self.rightChild=None

    def hasLeftChild(self):
        if self.leftChild==None:
            return False
        return True

    def hasRightChild(self):
        if self.rightChild==None:
            return False
        return True

    def hasBothChildren(self):
        if self.hasLeftChild() and self.hasRightChild():
            return True
        return False

    def hasOneChild(self):
        return self.hasLeftChild() ^ self.hasRightChild()
    
class BinaryTree():
    def __init__(self):
        self.root=None
        self.size=0

    '''
    def insert(self, key, value):
        if self.root==None:
            self.root=Node(key, value)
        else:
            self._insert(self.root)
        self.size=+1
        
    def _insert(self, currentNode):
        if
    
    #METHOD 2. FAILED MISERABLY
    def insert(self, key, value):
        if self.root==None:
            self.root=Node(key, value)
        else:
            self._insert(self.root, key, value)


    def _insert(self, curNode, key, value):
        if curNode.hasLeftChild()==False:
            curNode.leftChild=Node(key, value)
            break
        elif curNode.hasRightChild()==False:
            curNode.rightChild=Node(key, value)
            break
        self._insert(curNode.leftChild, key, value)
        self._insert(curNode.rightChild, key, value)
    '''
    
    def insert(self, key, value):
        if self.root==None:
            self.root=Node(key, value)
        else:
            self._insert(self.root,i=0)
            self.insert2(key, value)
            
    BT=[]
    def _insert(self, curNode,i=0):
        if curNode==None:
            return
        self.BT.append([])
        self.BT[i].append(curNode)
        self._insert(curNode.leftChild, i+1)
        self._insert(curNode.rightChild, i+1)

    def insert2(self, key, value):
        star=None
        for i in range(len(self.BT)):
            for j in range(len(self.BT[i])):
                if self.BT[i][j].hasBothChildren()==False:
                    if self.BT[i][j].hasLeftChild():
                        self.BT[i][j].rightChild=Node(key, value)
                        break
                    else:
                        self.BT[i][j].leftChild=Node(key, value)
                        break
                        
    def inOrderTraversal(self, curNode):
        if curNode==None:
            return
        self.inOrderTraversal(curNode.leftChild)
        print curNode.key
        self.inOrderTraversal(curNode.rightChild)

    BFS=[]
    def BSTBFS(self, curNode, i=0):
        if curNode==None:
            return
        self.BFS.append([])
        self.BFS[i].append(curNode.key)
        self.BSTBFS(curNode.leftChild, i+1)
        self.BSTBFS(curNode.rightChild, i+1)

test=BinaryTree()
test.insert(1,"one")
test.insert(2, "two")
test.insert(3, "three")
test.insert(4, "four")
test.insert(4, "four")
test.insert(5, "five")
test.insert(6, "six")
test.insert(7, "seven")
