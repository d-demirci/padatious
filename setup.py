#!/usr/bin/env python3

from setuptools import setup

setup(
    name='padatious',
    version='0.1.3',
    description='A neural network intent parser',
    url='http://github.com/MycroftAI/padatious',
    author='Matthew Scholefield',
    author_email='matthew331199@gmail.com',
    license='Apache-2.0',
    packages=[
        'padatious'
    ],
    install_requires=[
        'fann2',
        'xxhash'
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
         
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='intent-parser parser text text-processing',
    
)