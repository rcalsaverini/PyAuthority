import igraph
import random
from numpy import Inf

class Agent(object):
    def __init__(self, cognitiveIdx = 1.0, n = 10, p=0.5, m = None, topology = 'ErdosRenyi'):
        self.graph = self.initializeGraph(n = n, p = p, m = m, topology = topology)
        self.cognitiveIdx = cognitiveIdx

    def initializeGraph(self, n = 10, p = 0.5, m = None, topology = 'ErdosRenyi'):
        if topology == 'ErdosRenyi':
            if m is None:
                graph = igraph.Graph.Erdos_Renyi(n=n, p=p)
            else:
                graph = igraph.Graph.Erdos_Renyi(n=n, m=m)
        elif topology == 'Full':
            graph = igraph.Graph.Full(n=n)
        elif topology == 'Star':
            graph = igraph.Graph.Star(n=n, center=0)
        elif topology == 'Empty':
            graph = igraph.Graph.Erdos_Renyi(n=n, m=0)
        else:
            graph = igraph.Graph.Full(n=n)
        return graph

    def energy(self):
        return self.edgeOccupation() + self.cognitiveIdx * self.averagePathLength()

    def averagePathLength(self):
        if self.isConnected():
            return self.graph.average_path_length()
        else:
            return Inf

    def edgeOccupation(self):
        ne = float(self.graph.ecount())
        nv = float(self.graph.vcount())
        nTotalEdges = nv * (nv - 1)/ 2.0
        return ne / nTotalEdges

    def groupSize(self):
        return self.graph.vcount()

    def pluck(self):
        (i,j) = self.getRandomVertexPair()
        self.pluckEdge(i,j)

    def pluckTillConnected(self):
        self.pluck()
        while not self.isConnected():
            self.pluck()

    def isConnected(self):
        return self.graph.is_connected()

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

    def plot(self):
        igraph.plot(self.graph)

    def __str__(self):
        return str(self.graph)

