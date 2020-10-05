#!/usr/bin/python3
"""
class to get data by data
any created instance of this class
will be a pandas dataframe containing the data in
the given periode
"""


from fetchapi import ft
import pandas as pd



class Get(pd.DataFrame):


    def __init__(self, ticker, start, end):
        super().__init__()

        """
        :param strticker - name of the stock
        :param str start - date of starting
        :param str end - date of ending
        """
        self.ticker = ticker
        self.start = start
        self.end = end


    def Data(self, *args):
        """
        method to get all the data of a given stock
        of a specific data like only "Price", or "High"
        """

        df = ft(self.ticker)
        start_date = self.start
        end_date = self.end
        after = df.index >= pd.to_datetime(start_date)
        before = df.index <= pd.to_datetime(end_date)
        periode = after & before
        d_f = df.loc[periode]
        d_f = pd.DataFrame(d_f)
        if len(args) != 0:
            s =""
            for i in range(len(args)):
                if i == 0:
                    s += args[i]
            return pd.Series(d_f[s])
        return d_f


