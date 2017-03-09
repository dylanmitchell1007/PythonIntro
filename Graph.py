from Node import Node
class Graph:
    graph = []
    
    #def getneighbors(node,graph):
       

    def getnode(self, id, g):
        for node in g.graph:
            if id is node.id:
                return node
    def __init__(self, XBounds, YBounds):
        X = 0
        Y = 0
        for i in range(0, (XBounds * YBounds)):
            node = Node(i+1)
            node.setPos(0,0)
            self.graph.append(node)
        for node in self.graph:
            node.setPos(X, Y)
            X += 1
            if X == XBounds:
                X = 0
                Y += 1
            
 