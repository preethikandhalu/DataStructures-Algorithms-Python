#Assume you can't have two vertices with same key
import LinkedList as LL

class adjacencyListUndirected():
    def __init__(self):
        self.list=[]
        self.vertex=0
        self.edge=0

    def numberOfVertexes(self):
        return self.vertex

    def numberOfEdges(self):
        return self.edge

    def addVertex(self, key):
        self.list.append(LL.LinkedList(key))
        self.vertex+=1
     
    def isVertexInList(self, vertex):
        for i in range(len(self.list)):
            if self.list[i].head.data==vertex:
                return True
        return False

    def indexOfVertex(self, vertex):
        if self.isVertexInList(vertex):
            for i in range(len(self.list)):
                if self.list[i].head.data==vertex:
                    return i
        return 
    
    def areBothVerticesInList(self, vertex1, vertex2):
        v1=False
        v2=False
        for i in range(len(self.list)):
            if self.list[i].head.data==vertex1:
                v1=True
            if self.list[i].head.data==vertex2:
                v2=True
        if v1==False or v2==False:
            return False
        return True

    def indexOfVertices(self, vertex1, vertex2):
        if self.areBothVerticesInList(vertex1, vertex2):
            v1Index=-1
            v2Index=-1
            for i in range(len(self.list)):
                if self.list[i].head.data==vertex1:
                    v1Index=i
                if self.list[i].head.data==vertex2:
                    v2Index=i
            indexes={}
            indexes.update({"vertex1":v1Index,"vertex2":v2Index})
            return indexes
        return
    
    def addEdge(self, vertex1, vertex2):
        a=self.indexOfVertices(vertex1, vertex2)
        if a==None:
            return
        v1Index=a["vertex1"]
        v2Index=a["vertex2"]
        self.list[v1Index].insert(vertex2)
        self.list[v2Index].insert(vertex1)
        self.edge+=1
        
    def removeVertex(self, key):
        kIndex=-1
        #remove vertex
        for i in range(len(self.list)):
            if self.list[i].head.data==key:
                kIndex=i
                break
        self.list.pop(kIndex)
        #remove edges that connect to key
        for i in range(len(self.list)):
            self.list[i].deleteValue(key)
            
    def removeEdge(self, vertex1, vertex2):
        a=self.indexOfVertices(vertex1, vertex2)
        v1Index=a["vertex1"]
        v2Index=a["vertex2"]
        self.list[v1Index].deleteValue(vertex2)
        self.list[v2Index].deleteValue(vertex1)
    
    def printList(self):
        for i in range(len(self.list)):
            self.list[i].printList()


test=adjacencyListUndirected()
test.addVertex(1)
test.addVertex(2)
test.addVertex(3)
test.addVertex(4)
test.addVertex(5)
test.addEdge(1,2)
test.addEdge(1,5)
test.addEdge(5,2)
test.addEdge(5,4)
test.addEdge(2,4)
test.addEdge(2,3)
test.addEdge(3,4)
'''
test.printList()
test.removeVertex(2)
print "AFTER REMOVING VERTEX 2"
test.printList()
'''
