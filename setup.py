#!/usr/bin/python3
"""
main module to fetch data
from mapi
"""


import requests
import sys
import pandas as pd
ticker = sys.argv[1]
data = requests.get('http://127.0.0.1:8000/api/'+ticker)
my_data = data.json()
my_list = []
for line in my_data:
    my_list.append(line)
my_list = my_list[1:]
my_list = pd.DataFrame(my_list)
my_list.columns = ['Date', 'Price', 'Open', 'Low', 'High', 'Volume', 'Change']
my_list.set_index("Date", inplace=True)

print(my_list)






