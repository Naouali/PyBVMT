#!/usr/bin/python3
"""
setup for mapi package
"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mapi",
    version="0.0.2",
    author="NAOUALI Nebil",
    author_email="elnaoualinebil@gmail.com",
    description="Mapi api module",
    py_modules = ['fetchapi', 'mapi'], 
    package_dir = {'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'pandas>=1.0.0',
        'requests>= 2.20.0',
        ],
    extras_require = {
        'dev': [
            'pandas',
            'requests']
        },
    python_requires='>=3.6',
    )
