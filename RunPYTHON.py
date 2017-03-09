from Graph import Graph
from Node import Node

g = Graph(3,3)

node = g.getnode(9, g)
node.print_info()
# neighbors = get_neighbors(node, graph)
 #for nod in neighbors:
  #      nod.print_info()
for node in g.graph:
    node.print_info()

