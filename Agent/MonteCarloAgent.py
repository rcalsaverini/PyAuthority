from Agent import Agent
from numpy import exp
from numpy.random import uniform

class MonteCarloAgent(Agent):
    def __init__(self, n = 10, a = 1.0, beta = 1.0):
        alpha = float(n * (n-1)/2) * a
        super(MonteCarloAgent, self).__init__(n=10, topology='Star', cognitiveIdx = alpha)
        self.chooseLowestEnergyInitialState()
        self.beta = beta
        self.oldGraph = self.graph.copy()

    def metropolisStep(self):
        Eold = self.energy()
        self.proposeNewGraph()
        Enew = self.energy()
        if not self.acceptProposition(Eold, Enew):
            self.graph = self.oldGraph
            self.accept = 0.0
        else:
            self.accept = 1.0

    def proposeNewGraph(self, numPlucks=5):
        self.oldGraph = self.graph.copy()
        for i in xrange(numPlucks):
            self.pluckTillConnected()

    def acceptProposition(self, Eold, Enew):
        dE = Enew - Eold
        p = exp(-dE * self.beta)
        return uniform() < p


