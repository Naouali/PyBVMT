#!/usr/bin/python3
"""
main module to fetch data
from mapi
"""


import requests
import sys
import pandas as pd


def ft(ticker):
    """
    fetch data from mapi finance api
    and convert it to pandas dataframe
    args: tickername: string
    return: pandas dataframe
    """
    data = requests.get('https://bvmtapi.herokuapp.com/api/'+ticker)
    my_data = data.json()
    my_list = []
    for line in my_data:
        my_list.append(line)
    my_list = my_list[1:]
    my_list = pd.DataFrame(my_list)
    my_list.columns = ['Date',
                       'Close',
                       'Open',
                       'Low',
                       'High',
                       'Volume',
                       'Change']
    my_list[['Close',
        'Open',
        'Low',
        'High',
        'Volume',
        'Change']] = my_list[['Close',
            'Open',
            'Low',
            'High',
            'Volume',
            'Change']].apply(pd.to_numeric)
    my_list['Date'] = my_list['Date'].apply(pd.to_datetime)
    my_list.set_index("Date", inplace=True)

    return(my_list)


