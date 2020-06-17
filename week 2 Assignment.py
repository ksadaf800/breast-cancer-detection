#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[6]:


df=pd.read_excel(r"C:\Users\Lenovo\Downloads\data.xlsx")


# In[7]:


df


# In[8]:


# Step 1: Open the file in your python notebook, print first 5 rows of the dataset and mention what are the dependent and independent variables in the Data
df.head(5)


# In[9]:


#mention dependent and independent variable diagnosis will be our dependent variable and the rest of the columns will be our independent variables


# In[10]:


# Step 2: Find the statistical parameters of the Data that you have
df.describe()


# In[11]:


# Step 3: Find the shape of the Dataset in hand.
df.shape


# In[12]:


# Step 4: Find missing values from the Dataset
df.isnull().sum()


# In[13]:


# Step 5: Find the value count of B(Benign) and M(Malignant) cancer cells in the column "diagnosis" 
df['diagnosis'].value_counts()


# In[14]:


from sklearn.preprocessing import LabelEncoder
labelencoder_Y=LabelEncoder()
df.iloc[:,1]=labelencoder_Y.fit_transform(df.iloc[:,1].values)


# In[15]:


df.head(5)


# In[17]:


# Step 6: Creating a pairplot and mention the findings
# we will only create a pairplot of first 5 columns and write the findings.

pp=sns.pairplot(df.iloc[:,1:5])


# In[18]:


# Step 7: Create a correlation matrix and mention strongly, weakly and negatively correlated quantities.
df.corr()


# In[ ]:


#The Values which are close to 1 are strongly co related The Values which are close to -1 are negatively co related The Values which are close to 0 are weakly co related


# In[19]:


# (Optional) Step 8: Create a heatmap of the correlated features (helps in visualization)
sns.heatmap(df.corr(), annot=True,fmt="0.0%")


# In[ ]:




