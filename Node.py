
class Node:    
    def __init__(self, id):
        self.id = id

        
    def setPos(self, X, Y):
        self.Xpos = X
        self.Ypos = Y
    
    def print_info(self):
        print("Node" + str(self.id) + "  ("+ str(self.Xpos) + "," + str(self.Ypos) + ")")
