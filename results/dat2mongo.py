import csv
import pymongo

conn = pymongo.Connection()
collection = conn.doc.singlerun
sumCollection = conn.doc.sumSingleRun

cNames = ['n', 'alpha', 'beta', 'energy', 'davg', 'dmax', 'acceptance']
fname = './dataFiles/singleRun.dat'

def createFullResultsCollection():
    with open(fname, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            data = {k: float(v.strip()) for k,v in zip(cNames, row)}
            collection.insert(data)

def createSummarizedCollection():
    results = collection.aggregate({'$group' :
                                       {'_id': "$alpha", 'dmax' : {'$avg' : '$dmax'}
                                                       , 'davg' : {'$avg' : '$davg'}
                                                       , 'energy' : {'$avg' : '$energy'}
                                                       , 'acceptance' : {'$avg' : '$acceptance'}
                                       }
                                   })['result']
    for doc in results:
        sumCollection.insert(doc)
createFullResultsCollection()
createSummarizedCollection()
