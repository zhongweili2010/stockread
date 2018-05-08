# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:23:38 2018

@author: c_zhonli
"""

import requests
import json
import pprint
import pandas as pd

class api:
    def __init__(self,function="TIME_SERIES_INTRADAY",symbol="MSFT",interval="1min",outputsize="compact",datatype="jason",apikey="IQQ6W4ESX1DDHQNB"):
        self.function=function
        self.symbol=symbol
        self.interval=interval
        self.outputsize=outputsize
        self.datatype=datatype
        self.apikey=apikey


    def get_function(self):
        return self.function
    def get_interval(self):
        return self.interval
    def get_url(self):
        return "https://www.alphavantage.co/query?function=" + self.function\
                   + "&symbol=" + self.symbol\
                   + "&interval=" + self.interval\
                   + "&outputsize=" + self.outputsize\
                   + "&apikey=" + self.apikey
     

handle_to_api = api()

connection =  requests.get(handle_to_api.get_url())

print("status code: " + str(connection.status_code))
#print(type(connection.content))
content = json.loads(connection.content.decode())
#print(type(content))
#pprint.PrettyPrinter().pprint(content["Meta Data"])
data = pd.DataFrame(content)
#data = pd.DataFrame.from_dict(content["Time Series (" + handle_to_api.get_interval()+")"], orient='row')
print(data)
