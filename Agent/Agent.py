import igraph
class Agent(object):
    def __init__(self, n = 10):
        self.graph = igraph.Graph.Erdos_Renyi(n=n, p=0.5)

    def pluck(self):
        (i,j) = self.getRandomVertexPair()
        self.pluckEdge(i,j)

    def __str__(self):
        return str(self.graph)

