#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
setup(
        name     = 'AuthoritySimulation',
        version  = '0.1' ,
        author   = 'Rafael S. Calsaverini',
        author_email = 'rafael.calsaverini@gmail.com',
        packages = ['Agent'],
        license  = 'Creative Commons Attribution-Share Alike license',
        description = 'Authority Simulation',
        install_requires = [
            "argparse",
            "python-igraph",
            "numpy"
            ],
        entry_points = { 'console_scripts' : ["runAuthorityMCMC= Agent:processArgumentsAndRun" ]},
        )
