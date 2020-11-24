#!/usr/bin/env python
# coding: utf-8

# # Cryptocurrency prices
# 
# * **Filename:**  `cryptocurrencies.csv`
# * **Description:** Cryptocurrency prices for a handful of coins over time.
# * **Source:** https://coinmarketcap.com/all/views/all/ but from a million years ago (I cut and pasted, honestly)
# 
# ### Make a chart of bitcoin's high, on a weekly basis
# 
# You might want to do the cherry blossoms homework first, or at least read the part about `format=` and `pd.to_datetime`.
# 
# *Yes, that's the entire assignment. It isn't an exciting dataset, but it's just dirty enough to make charting this a useful experience.*

# In[1]:


import pandas as pd
from pprintpp import pprint as pp
import numpy as np 

df = pd.read_csv("cryptocurrencies.csv")
df_bitcoin = df[df.coin == "BTC"]
df_bitcoin


# In[2]:


#Put date to datetime
df_bitcoin.date = pd.to_datetime(df_bitcoin.date)


# In[3]:


#Get rid of commas in the high column so we can change its type to float
df_bitcoin.high = df_bitcoin.high.str.replace(",", "")

#Change to float
df_bitcoin.high = df_bitcoin.high.astype(float)


# In[4]:


#Verify the column types
df_bitcoin.dtypes


# In[5]:


#Set the index to date
df_bitcoin = df_bitcoin.set_index('date')


# In[6]:


#df_bitcoin to verify it all looks right


# In[7]:


print("Max Weekly Bitcoin Price, February 2018 to March 2018")
df_bitcoin.resample('W').high.max().plot()

