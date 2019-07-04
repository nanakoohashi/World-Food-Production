#!/usr/bin/env python
# coding: utf-8

# # Who eats the food we grow?

# [**The Food and Agriculture Organization of the United Nations**](http://www.fao.org/faostat/en/#home) provides free access to food and agriculture data for over 245 countries and territories, from the year 1961 to the most recent update.

# ## Gather

# In[1]:

import pandas as pd
import zipfile
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
% matplotlib inline


# In[2]:
df = pd.read_csv('world-foodfeed-production.csv', encoding = "ISO-8859-1")
df


# ## Assess

# In[3]:

df.head()


# In[4]:

df.shape


# In[5]:

df.info()


# In[6]:

df.dtypes


# In[7]:
df.describe()


# In[8]:

# View missing value count for each feature.
df.isnull().sum()


# #### Structure of Dataset
There are 21,477 entries in this dataset with 58 features (Area Abbreviation, Area Code, Area, Item Code, Item, Element Code, Element, latitude, longitude, Years 1961 to 2013).


# #### Main feature(s) of interest in the dataset
- Origin of food products.
- Change in food production by year.


# #### What features in the dataset do you think will help support your investigation into your feature(s) of interest?

# ### Issues 
- Remove `Area Abbreviation`, `Area Code`, `Item Code`, `Element Code`, `latitude`, `longitude`, and `Unit` columns.
- Remove `feed` entries in `Element` column.
- Remove Y from year columns.


# ## Clean


# In[9]:

# make copy of data set
df1= df.copy()


# In[10]:

# drop 'Area Abbreviation' column
df1.drop('Area Abbreviation', axis=1, inplace=True)
df1


# In[11]:

# drop 'Area Code' column
df1.drop('Area Code', axis=1, inplace=True)
df1


# In[12]:

# drop 'Item Code' column
df1.drop('Item Code', axis=1, inplace=True)
df1


# In[13]:

# drop 'Element Code' column
df1.drop('Element Code', axis=1, inplace=True)
df1


# In[14]:

# drop 'Unit' column
df1.drop('Unit', axis=1, inplace=True)
df1


# In[15]:

# drop 'latitude' column
df1.drop('latitude', axis=1, inplace=True)
df1


# In[16]:

# drop 'longitude' column
df1.drop('longitude', axis=1, inplace=True)
df1


# In[17]:

# select elements that = "Food"
df2 = df1.query('Element == "Food"')
df2   


# In[18]:

df2.columns.unique()


# In[19]:

# Remove "Y" from all year columns
df2.columns = df2.columns.str.replace("Y", "")
df2


# In[20]:

df2.Item.unique()
