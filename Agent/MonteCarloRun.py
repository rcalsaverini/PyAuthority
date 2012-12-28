from MonteCarloAgent import MonteCarloAgent
from numpy import mean

class MonteCarloRun(MonteCarloAgent):

    def run(self, burn = 10000, steps = 100000, thin = 2):
        self.burnInSteps(burn)
        for obsValues in self.liveSteps(steps, thin):
            yield obsValues

    def burnInSteps(self, burn):
        for step in xrange(burn):
            self.metropolisStep()

    def liveSteps(self, steps, thin):
        for step in xrange(steps):
            self.metropolisStep()
            if step % thin == 0:
                yield [(name, function(self)) for (name, function) in self.calculateObservables()]

    def calculateObservables(self):
        self.observableNames = ['energy', 'avgDegree', 'maxDegree', 'acceptance']
        self.observableFunctions = [lambda x: x.energy(), lambda x: mean(x.graph.degree()), lambda x: max(x.graph.degree()), lambda x: x.accept]
        for name, function in zip(self.observableNames, self.observableFunctions):
            yield name, function

