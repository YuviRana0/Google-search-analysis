# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:02:08 2024

@author: win 10
"""

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import time

Trending_topics = TrendReq(hl='en-US', tz=360)

kw_list=["Diwali"]
Trending_topics.build_payload(kw_list,cat=0, timeframe='today 12-m')
time.sleep(5) # Wait for 5 second

data = Trending_topics.interest_over_time()
data = data.sort_values(by="Diwali", ascending = False)
data = data.head(10)
print("When the topic was most searched from today 12 noon:")
print(data)
kw_list = ["Diwali"]
Trending_topics.build_payload(kw_list, cat=0, timeframe='2018-01-01 2018-02-01', geo='', gprop='')
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Diwali", ascending = False)
data = data.head(10)
print("When the topic was most searched hourly:")
print(data)
data = Trending_topics.interest_by_region()
data = data.sort_values(by="Diwali", 
                        ascending = False)
data = data.head(10)
print("Topic most searched in the regions")
print(data)
    
data.reset_index().plot(x='geoName', y='Diwali',
                        figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()
