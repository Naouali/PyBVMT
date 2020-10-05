#!/usr/bin/python3
"""
setup for mapi package
"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyBVMT",
    version="0.0.2",
    author="NAOUALI Nebil",
    author_email="elnaoualinebil@gmail.com",
    description="BVMT API",
    long_description_content_type="text/markdown",
    py_modules = ['fetchapi', 'pyBVMT'],
    package_dir = {'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'pandas>=1.0.0',
        'requests>= 2.20.0',
        'matplotlib>= 3.0.0',
        ],
    extras_require = {
        'dev': [
            'pandas',
            'requests']
        },
    python_requires='>=3.5',
    )
