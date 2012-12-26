from Agent import MonteCarloAgent
from numpy import mean, linspace

def aggregateMeans(meandict, datadict):
    n = meandict.get('count', 0.0)
    meandict['count'] = n + 1
    for k, v in datadict.items():
        meandict[k] = (meandict.get(k, 0.0) * float(n) + float(v))/float(n+1)


def runMetropolis(mcmcAgent, burn = 2000, steps = 10000):
    for step in xrange(burn):
        mcmcAgent.metropolisStep()
    meanObs = {}
    for step in xrange(steps):
        mcmcAgent.metropolisStep()
        aggregateMeans(meanObs, mcmcAgent.calculateObservables())
    return meanObs

observables = {'energy': lambda x : x.energy(),
               'avg degree': lambda x: mean(x.graph.degree()),
               'max degree': lambda x: max(x.graph.degree()),
               'acceptance': lambda x: x.accept,
               }

obsnames = observables.keys()
line = '\t'.join(['{n:8}'.format(n=n) for n in obsnames])
print '#{a:>8}'.format(a='a'),'\t', line

for a in linspace(0, 1, 101):
    mcmcAgent = MonteCarloAgent(n = 15, a = a, beta = 6.0, observables=observables)
    avgs = runMetropolis(mcmcAgent)
    line = '\t'.join(['{v:8.3f}'.format(v = avgs[n]) for n in obsnames])
    print '{a:8.3}'.format(a=a),'\t', line

