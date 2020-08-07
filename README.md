# [BVMTAPI](https://bvmtapi.herokuapp.com/)
<br>

## Introduction:
> bvmtapi is a python package that allow user to use [Mapi](https://bvmtapi.herokuapp.com/) api directly to fecth financial data about any given stock indexed in the Tunisian Stock exchange without writing any requests.

## Author:
> [NAOUALI Nebil](https://www.linkedin.com/in/noualinebil/)

## Installation:
Use the package manager [pip](https://pypi.org/project/bvmtapi/) to install bvmtapi
 ```bash
 pip install bvmtapi
 ```
## Usage
 ```python
 from mapi import Get
 biat = Get('biat', '2015-01-01', '2017-01-01')
 biat.Data()
 ```
#### Output

| Date       | Close | Open   |  Low  |  High | Vol   | 
| ---------- | ----- | ------ | ----- | ----- | ----- |    
| 2016-12-30 | 89.75 |  89.90 | 89.90 | 88.20 | 00.14 |  
| 2016-12-29 | 88.20 |  88.00 | 88.20 | 88.00 | 15.75 |  
| 2016-12-28 | 87.99 |  88.00 | 88.00 | 87.99 | 10.72 |  
| 2016-12-27 | 88.00 |  88.00 | 88.00 | 86.00 | 01.30 |  
| 2016-12-26 | 88.00 |  88.00 | 88.00 | 88.00 | 00.59 |  
| 2015-01-08 | 79.00 |  78.00 | 79.70 | 78.00 | 00.77 |  
| 2015-01-07 | 79.70 |  79.00 | 79.70 | 79.00 | 00.21 |  
| 2015-01-06 | 79.49 |  78.00 | 79.49 | 78.00 | 00.27 |  
| 2015-01-05 | 79.79 |  78.25 | 79.79 | 78.25 | 00.44 |  
| 2015-01-02 | 78.02 |  79.50 | 79.90 | 78.02 | 01.31 |  


