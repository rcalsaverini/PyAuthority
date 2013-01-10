import csv
import pymongo

conn = pymongo.Connection()
collection = conn.doc.singlerun

cNames = ['n', 'alpha', 'beta', 'dmax', 'davg', 'energy', 'acceptance']
fname = 'singleRun.dat'


with open(fname, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        data = {k: float(v.strip()) for k,v in zip(cNames, row)}
        collection.insert(data)
