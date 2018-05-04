# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:23:38 2018

@author: c_zhonli
"""

import requests
import json

class stock_data():
    def __init__(self):
        self.function="TIME_SERIES_INTRADAY"
        self.symbol="MSFT"
        self.interval="1min"
        self.outputsize = "compact"
        self.datatype="jason"
        self.apikey="IQQ6W4ESX1DDHQNB"
     
     
     


connection =  requests.get("https://api.ethplorer.io/getTokenInfo/0xff71cb760666ab06aa73f34995b42dd4b85ea07b?apiKey=freekey")
print(connection.status_code)
#print(type(connection.content))
content = json.loads(connection.content.decode())
print(content["address"])

