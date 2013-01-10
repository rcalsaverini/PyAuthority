#/usr/bin/env python
from numpy import linspace

def stepTimeEstimate(nsteps, burnin):
    return (nsteps + burnin) / 1000 * 0.5

n = 15
nsteps = 2000 * n * (n-1)/2
burnin = 2000 * n * (n-1)/2
thin = n
beta = 10.0
totalTimeEstimate = 0

for alpha in linspace(0, 2.0, 101):
    totalTimeEstimate += stepTimeEstimate(nsteps, burnin)
    print n, alpha, beta, nsteps, burnin, thin

print "time estimate: ", totalTimeEstimate/3600.0, "hours"
