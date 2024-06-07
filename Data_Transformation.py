#!/usr/bin/env python
# coding: utf-8

# # Data Transformation

# Data Cleaning and Preprocessing

# In[6]:


# Drop 'CustomerID' column as it's not useful for analysis
customer_df.drop(columns=['CustomerID'], inplace=True)


# In[7]:


# Check for missing values
print(customer_df.isna().sum())


# In[31]:


# Convert 'Gender' to dummy variables
dummies = pd.get_dummies(customer_df['Gender'], dtype=int)
customer_newdf = pd.concat([customer_df, dummies], axis='columns')
customer_newdf.drop(columns=['Gender'], inplace=True)


# In[32]:


# Standardize the data
scaler = StandardScaler()
scaler.fit(customer_newdf)
scaled_data = scaler.transform(customer_newdf)
customer_scaled = pd.DataFrame(data = scaled_data, columns = customer_newdf.columns)
print(customer_scaled)

