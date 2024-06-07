#!/usr/bin/env python
# coding: utf-8

# # Data Ingestion

# Importing Libraries and Loading data 
# 

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler


# In[2]:


def set_size_style(width, height, style=None):
    plt.figure(figsize=(width, height))
    if style != None:
        sns.set_style(style)

def customize_plot(plot, title:str, xlabel:str,  ylabel:str, title_font:int, label_font:int):
    plot.set_title(title, fontsize = title_font, weight='bold')
    plot.set_xlabel(xlabel, fontsize = label_font, weight='bold')
    plot.set_ylabel(ylabel, fontsize = label_font, weight='bold')


# In[3]:


customer_df = pd.read_csv('Mall_Customers.csv')
customer_df.head()


# In[4]:


customer_df.shape


# In[5]:


customer_df.describe()

