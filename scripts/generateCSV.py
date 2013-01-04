#/usr/bin/env python
from numpy import linspace

n = 15
nsteps = 1000000
burnin = 100000
thin = 3
beta = 7.0
for beta in linspace(0.01, 10.0, 21):
    for n in [10, 12, 14, 16, 18, 20]:
        for alpha in linspace(0, 2.0, 101):
            print n, alpha, beta, nsteps, burnin, thin
