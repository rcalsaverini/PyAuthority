from scipy.optimize import fminbound
from numpy import pi, log, linspace
from sys import stderr
import pymongo

conn = pymongo.Connection()
coll = conn.doc.sumSingleRun

def entropy(p, n):
    ne = float(n * (n-1)/2)
    return 0.5 * log (2.0 * pi * ne * p * (1-p))

def energy(p, a, n):
    return p + a * log(n-1)/(log(p) + log(n-1))

def freeEnergy(p, a, n, T):
    return energy(p, a, n) - T * entropy(p, n)

def maxFreeEnergy(a, n, T):
    minusFreeEnergy = lambda p : freeEnergy(p, a, n, T)
    pstar, fval, ierr, _ = fminbound(minusFreeEnergy, 0.0, 1.0, full_output = 1)
    if ierr == 0:
        return pstar, fval
    else:
        raise ValueError("fminbound not converged")

def getDAvg(a = 0.0):
    try:
        davg = coll.find_one({'_id': a})['davg']
    except:
        davg = 0.0
    return davg

n = 15
beta = 10.0
for a in linspace(0.0, 2.0, 101):
    try:
        pstar, fval = maxFreeEnergy(a, n, 1.0/beta)
    except ValueError, e:
        print >>stderr, e
    print a, pstar, getDAvg(a)/(n-1.0)
