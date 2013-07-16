import pymongo
from pylab import *

conn = pymongo.Connection()
coll = conn.doc.sumSingleRun

def getData(var = 'davg', getX = False):
    x, y = [], []
    cursor = coll.find({'_id': {'$gt': 0.1}}, {'_id': 1, var:1})
    for item in cursor.sort('_id',1):
        x.append(item['_id'])
        y.append(item[var])
    return (x, y) if getX else y

alpha, davg = getData(var = 'davg', getX = True)
dmax = getData(var='dmax')
plot(alpha, davg)
plot(alpha, dmax)
show()
