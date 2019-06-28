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
