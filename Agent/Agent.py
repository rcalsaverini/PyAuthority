import igraph
import random

class Agent(object):
    def __init__(self, n = 10, p=0.5):
        self.graph = igraph.Graph.Erdos_Renyi(n=n, p=p)

    def groupSize(self):
        return self.graph.vcount()

    def pluck(self):
        (i,j) = self.getRandomVertexPair()
        self.pluckEdge(i,j)

    def pluckTillConnected(self):
        pass

    def getRandomVertexPair(self):
        n = self.graph.vcount()
        return random.sample(xrange(n),2)

    def pluckEdge(self, i,j):
        try:
            self.removeEdge(i,j)
        except igraph.InternalError:
            self.addEdge(i,j)

    def removeEdge(self, i, j):
        self.graph.delete_edges([(i,j)])

    def addEdge(self, i, j):
        self.graph.add_edge(i, j)

    def __str__(self):
        return str(self.graph)

