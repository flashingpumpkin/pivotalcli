#!/usr/bin/env python

import pivotalcli
from setuptools import setup, find_packages



setup(
    name='Pivotal Cli',
    version=pivotalcli.__version__,
    description='Command line client for Pivotal Tracker',
    long_description=open('README.md').read(),
    author='Alen Mujezinovic',
    author_email='alen@caffeinehit.com',
    packages=find_packages(),
    install_requires=[
        "docopt   == 0.4.1",
        "requests == 0.12.1",        
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'pivotalcli = pivotalcli.cli:main',
        ]   
    }

)
