
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()


# In[3]:


data = pd.read_csv('f150data.csv')


# In[4]:


data.shape


# In[12]:


data.info()


# In[11]:


data.describe(include='all')

