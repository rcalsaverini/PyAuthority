import pandas
from pylab import show, figure

avgResults = pandas.read_csv('./dataFiles/avgResults.dat', sep = ' ', names = ['n', 'a', 'beta', 'eng', 'davg', 'dmax', 'accept'], index_col = ['n', 'a', 'beta'] )
counts = pandas.read_csv('resultCount.dat', sep = ' ', names = ['n', 'a', 'beta', 'count'], index_col = ['n', 'a', 'beta'] )['count']

counts.select(lambda (n, a, beta) : (n == 10) and (beta == 10.0))
counts.plot()
show()


