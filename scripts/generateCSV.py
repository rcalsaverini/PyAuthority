#/usr/bin/env python
from numpy import linspace

n = 15
nsteps = 1000
burnin = 100
thin = 1
beta = 7.0
for alpha in linspace(0, 2.0, 101):
    print n, alpha, beta, nsteps, burnin, thin
