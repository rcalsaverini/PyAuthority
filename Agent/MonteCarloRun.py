from MonteCarloAgent import MonteCarloAgent
from numpy import mean
import argparse
import sys

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


def readInput(filein):
    for line in filein:
        numAgents, alpha, beta, burnIn, mcSteps, thin = line.split()
        yield int(numAgents), float(alpha), float(beta), int(burnIn), int(mcSteps), int(thin)


def readFromStdinAndRun():
    for n, alpha, beta, burnIn, mcSteps, thin in readInput(sys.stdin):
        if thin < 1:
            thin = 1
        mcmc = MonteCarloRun(n = n, a = alpha, beta = beta)
        for results in mcmc.runSimulation(burn = burnIn, steps = mcSteps, thin = thin):
            toPrint = dict(results)
            toPrint.update({'n': n, 'a': alpha, 'beta': beta})
            print "{n} {a} {beta} {energy} {avgDegree} {maxDegree} {acceptance}".format(**toPrint)



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
    readFromStdinAndRun()

