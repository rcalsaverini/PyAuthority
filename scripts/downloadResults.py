import boto
import os

s3 = boto.connect_s3('AKIAINVE7PR5AJ5UJBBA', 'W8xugFQDxiypK/wgjSkpZ/n3eAHD83QzXy0LY6We')
bucket = s3.lookup('doutorado')
dirs = ['avgResults', 'percentile05', 'percentile95', 'resultCount', 'stddevResults']

def downloadBucketFolder(bucket, dirname = 'avgResults', destination = '../results/'):
    keys = bucket.list(prefix = dirname)
    for key in keys:
       print "downloading {fname}... ".format(fname=destination + key.name),
       key.get_contents_to_filename(destination + key.name)
       print "ok!"


def ensurePath(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

for folder in dirs:
    ensurePath('../results/{folder}'.format(folder=folder))
    print "downloading {folder}".format(folder = folder)
    downloadBucketFolder(bucket, dirname = folder)
