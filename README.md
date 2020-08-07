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

| Date| Close  | Open |   Low |  High | Volume | Change|

| 2016-12-30 | 89.75|  89.90|  89.90|   88.20|     0.14|     1.76| 
| 2016-12-29 | 88.20|  88.00|  88.20|   88.00|    15.75 |    0.24| 
| 2016-12-28 | 87.99|  88.00|  88.00|   87.99|    10.72 |   -0.01| 
| 2016-12-27 | 88.00|  88.00|  88.00|   86.00|     1.30 |    0.00| 
| 2016-12-26 | 88.00| 88.00 | 88.00 |  88.00 |    0.59 |    0.00| 
| ...        |  ... |   ... |    ...  |   ...    |  ...   |   ...| 
| 2015-01-08 |79.00 | 78.00 | 79.70 |  78.00 |    0.77|    -0.88| 
| 2015-01-07 | 79.70|  79.00|  79.70|   79.00|     0.21|     0.26| 
| 2015-01-06 | 79.49|  78.00| 79.49  | 78.00 |    0.27|    -0.38| 
| 2015-01-05 | 79.79|  78.25| 79.79  | 78.25 |    0.44|     2.27| 
| 2015-01-02 | 78.02|  79.50| 79.90 |  78.02 |    1.31|     0.03| 

