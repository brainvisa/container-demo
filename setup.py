import os

from setuptools import setup, find_packages

setup(
    name='container_demo',
    version='1.0',
    description='Very simple python software used to illustrate Singularity or Docker usage',
    package_dir={'': 'python'},
    packages=find_packages('python'),
    scripts=['bin/cdemo_threshold'],
    install_requires=[
        'nibabel',
        'numpy',
    ]
)
