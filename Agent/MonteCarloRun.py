from MonteCarloAgent import MonteCarloAgent
from numpy import mean
import argparse

class MonteCarloRun(MonteCarloAgent):

    def runSimulation(self, burn = 10000, steps = 100000, thin = 2):
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

def processArgumentsAndRun():
    parser = argparse.ArgumentParser(prog = "runAuthorityMCMC")
    parser.add_argument('numAgents', type=int)
    parser.add_argument('normalizedBrainCapacity', type=float)
    parser.add_argument('ecologicalPressure', type=float)
    parser.add_argument('burnInSteps', type=int)
    parser.add_argument('monteCarloSteps', type=int)
    parser.add_argument('thiningRatio', type=int)
    args = parser.parse_args()
    mcmc = MonteCarloRun(n = args.numAgents, a = args.normalizedBrainCapacity, beta = args.ecologicalPressure)
    for results in mcmc.runSimulation(burn = args.burnInSteps, steps = args.monteCarloSteps, thin = args.thiningRatio):
        line = ' '.join(["{value}".format(value = value) for (_, value) in results])
        print args.numAgents, args.normalizedBrainCapacity, args.ecologicalPressure, line


if __name__ == '__main__':
    processArgumentsAndRun()

