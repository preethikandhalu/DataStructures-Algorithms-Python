import adjacencyListUndirected as graph

#Breadth First Search

'''
Input: Graph G = (V, E), either directed or undirected, and source vertex, s in V.
Output: v.d = distance (smallest # of edges) from s to v , for all v in V
'''

def BFS(AdjList, sourceVertex):
    vertexNo=AdjList.numberOfVertexes()
    distance=[]
    visited=[]
    vertexes=[]
    for i in range(vertexNo):
        distance.append(-1)
        visited.append(False)
        vertexes.append(AdjList.list[i].head.data)
    visited[vertexes.index(sourceVertex)]=True
    distance[vertexes.index(sourceVertex)]=0
    dist=0
    while False in visited:
        wvfront=[]
        wvfront.append(AdjList.indexOfVertex(sourceVertex))
        #Get adjacent vertexes' keys
        for i in wvfront:
            temp=AdjList.list[i].head
            while temp:
                wvfront.append(temp.data)
                temp=temp.next_node
        #convert to index
        for i in wvfront:
            wvfront[i]=AdjList.indexOfVertex(i)
        for i in wvfront:
            distance[i]=dist
        dist+=1
        
        
        
        
        
#TEST
test=graph.adjacencyListUndirected()
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
