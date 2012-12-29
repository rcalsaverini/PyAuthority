#!/bin/bash
sudo aptitude update
sudo aptitude install build-essential libxml2-dev libglpk-dev libgmp3-dev libblas-dev liblapack-dev libarpack2-dev python-dev python-numpy python-pip git
wget http://dl.dropbox.com/u/875394/igraph.tgz
tar -xvzf igraph.tgz

cd igraph-0.6
./configure
make
sudo make install

cd python-igraph-0.6
sudo python setup.py install