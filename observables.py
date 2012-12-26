from Agent import MonteCarloAgent
from numpy import mean

def aggregateMeans(meandict, datadict):
    n = meandict.get('count', 0.0)
    meandict['count'] = n + 1
    for k, v in datadict.items():
        meandict[k] = (meandict.get(k, 0.0) * float(n) + float(v))/float(n+1)

observables = {'energy': lambda x : x.energy(),
               'avg degree': lambda x: mean(x.graph.degree()),
               'max degree': lambda x: max(x.graph.degree()),
               'acceptance': lambda x: x.accept,
               }

mcmcAgent = MonteCarloAgent(n = 15, a = 0.5, beta = 8.0, observables = observables)
meanobs = {}
for step in xrange(100000):
    mcmcAgent.metropolisStep()
    aggregateMeans(meanobs, mcmcAgent.calculateObservables())
    if step % 1000 == 0:
        for n,v in meanobs.items():
            print '{n}:  {v}, '.format(n=n,v=v),
        print ''
        meanobs= {}
    if step % 10000 == 0:
        mcmcAgent.plot()


