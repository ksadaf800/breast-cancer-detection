#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
# In[4]:
# Q1 Create an array having consecutive natural numbers of size 6x3 and print it.
arr=np.arange(18).reshape(6,3)
print("array of 6 X 3 matrix : \n {}".format(arr))
# In[5]:
import pandas as pd
# In[7]:
df=pd.read_excel(r"C:\Users\Lenovo\Downloads\Week 1 Dataset.xlsx")
# In[8]:
print(df)
# In[9]:
df


# In[14]:

# Q2 Rename all the coumns in the dataset as per your wish and save it in another dataframe and name it df2
df2=df.rename(columns={"State":"State_name"})
df2
# In[17]:
df2=df.rename(columns={"State":"State_name","Income per month":"Income","Age":"age","Number of siblings":"siblings number"})
df2


# In[18]:

# Q3: After you have created df2, make the same changes in the original dataframe using the inplace
df.rename(columns={"State":"State_name","Income per month":"Income","Age":"age","Number of siblings":"siblings number"},inplace=True)
df


# In[20]:

# Q4: Show only the columns information, sex and number of siblings.
df[["Sex","siblings number"]]


# In[21]:

# Q5: Use iloc method to print data from column 1 to 4 and rows 3 to 9
df.iloc[3:9,1:4]


# In[22]:

# Q6: Find the total value count of number of siblings in the given dataset
df["siblings number"].value_counts()


# In[24]:
import seaborn as sns
# In[30]:
sns.heatmap(df.corr(), annot=True,fmt="0.0%")

"""# Q7: What are dependent and independent varibles in our dataset?
What you want to predict is the dependent variable i.e y, and the variable affecting the model is x(Independent variable ). Age and gender can be the independent variable whereas Income per month and No of siblings can be the dependent variable

# Q8: Mention all your finding from the above given heatmap.
A heatmap is a graphical representation of data that uses a system of color-coding to represent different values. In this Scenario Income per Month is plot against number of siblings where we see a dark color whereas age is plot against number of siblings again where the color is quite light.
"""