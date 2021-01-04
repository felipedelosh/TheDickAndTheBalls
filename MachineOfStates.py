"""
Machine of states 

You need first insert a nodes then you insert a edges and last you define initial point
if you need mouve only insert a key

"""
__author__      = "FelipedelosH"

class MachineOfStates:
    def __init__(self):
        self.pointer = None # Say what node stay currently
        self.node = []
        self.edges = {}

    def addNode(self, x):
        if x not in self.node:
            self.node.append(x)

    def addConection(self, a, b, key):
        """
        a = origin node
        b = next node
        key = key to jump
        """
        if a in self.node and b in self.node:
            if a in self.edges.keys():
                conection = self.edges[a]
                conection.append((b, key))
            else:
                conection = [(b, key)]
                self.edges[a] = conection

    def setInitialPointer(self, node):
        """
        The machine needs initial point to move
        """
        if node in self.node:
            self.pointer = node


    def insertSimbol(self, key):
        """
        key is a simbol to insert in machine
        move a pointer
        """
        if self.pointer != None:
            for i in self.edges[self.pointer]:
                if key == i[1]:
                    self.pointer = i[0]