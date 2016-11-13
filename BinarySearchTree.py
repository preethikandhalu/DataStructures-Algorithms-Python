'''REFERENCES'''
#http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html#lst-bst1
#http://datastructuresnotes.blogspot.com/2009/02/binary-tree-traversal-preorder-inorder.html
#https://www.cs.swarthmore.edu/~newhall/unixhelp/Java_bst.pdf

'''
NODE ATTRIBUTES AND FUNCTIONS
ATTRIBUTES
- parent
- key
- value
- leftChild
- rightChild
FUNCTIONS
- __init__()
- hasLeftChild()
- hasRightChild()
- isLeftChild()
- isRightChild()
- isRoot()
- isLeaf()
- hasAnyChildren()
- hasBothChildren()
'''
class Node:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.parent = parent
        self.key = key
        self.value=val
        self.leftChild = left
        self.rightChild = right

    def hasLeftChild(self):
        if self.leftChild:
            return True
        return False

    def hasRightChild(self):
        if self.rightChild:
            return True
        return False
    
    def isLeftChild(self):
        if self.parent and self.parent.leftChild == self:
            return True
        return False

    def isRightChild(self):
        if self.parent and self.parent.rightChild == self:
            return True
        return False

    def isRoot(self):
        if not self.parent:
            return True
        return False

    def isLeaf(self):
        if self.leftChild==None and self.rightChild==None and self.parent:
            return True
        return False
   
    def hasAnyChildren(self):
        if self.rightChild or self.leftChild:
            return True
        return False

    def hasBothChildren(self):
        if self.rightChild and self.leftChild:
            return True
        return False

'''
BINARY SEARCH TREE ATTRIBUTES AND FUNCTIONS
ATTRIBUTES
- root
- size
FUNCTIONS
- __init__()
- length()
- put()
- _put()
- __setitem__()
- get()
- _get()
- __getitem__()
- __contains__()
- search()
- findMin()
- findMax()
- inOrderTraversal()
- preOrderTraversal()
- postOrderTraversal()
'''
class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size = self.size + 1

    def _put(self,key,val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key,val,parent=currentNode)

    #Overload [] operator for assignment
    #__setitem__ method call the put method.
    #EX. myZipTree['Plymouth'] = 55446, just like a Python dictionary
    def __setitem__(self,k,v):
        self.put(k,v)

    #Get value associated with key, if there is one
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.value
            return None
        return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    #Can write statements like this --> z = myZipTree['Fargo']. 
    def __getitem__(self,key):
        return self.get(key)
    
    #Returns True if tree contains key. False, otherwise.
    #__contains__ overloads  in operator
    #if 'Northfield' in myZipTree:
    #   print("oom ya ya")
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
        
    #METHOD 2 FOR GET
    def search(self, key, currentNode):
        if currentNode==None:
            return
        elif currentNode.key==key:
            return currentNode.value
        elif currentNode.key>key:
            return self.search(key, currentNode.leftChild)
        else:
            return self.search(key, currentNode.rightChild)
        
    def findMin(self):
        currentNode=self.root
        if currentNode:
            while currentNode.hasLeftChild():
                currentNode=currentNode.leftChild
            return currentNode.key
        else:
            return
    
    def findMax(self):
        currentNode=self.root
        if currentNode:
            while currentNode.hasRightChild():
                currentNode=currentNode.rightChild
            return currentNode.key
        else:
            return

#Input: root node of tree
# 2 1 3: Left  Root  Right
def inOrderTraversal(Node):
    print "In-order traversal"
    inOT(Node)
    
def inOT(Node):
    if Node==None:
        return
    #Node=Node.root
    inOT(Node.leftChild)
    print Node.key
    inOT(Node.rightChild)

# 2 3 1: Left  Right  Root
def postOrderTraversal(Node):
    print "Post-order traversal"
    poOT(Node)
    
def poOT(Node):
    if Node==None:
        return
    poOT(Node.leftChild)
    poOT(Node.rightChild)
    print Node.key

# 1 2 3: Root  Left  Right
def preOrderTraversal(Node):
    print "Pre-order traversal"
    prOT(Node)
    
def prOT(Node):
    if Node==None:
        return
    print Node.key
    prOT(Node.leftChild)
    prOT(Node.rightChild)


a=BinarySearchTree()
a.put(7,'seven')
a.put(1,'one')
a.put(9,'nine')
a.put(0,'zero')
a.put(3,'three')
a.put(2,'two')
a.put(5,'five')
a.put(4,'four')
a.put(6,'six')
a.put(8,'eight')
a.put(10,'ten')

