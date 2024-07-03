#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas
pip install scipy


# In[2]:


import pandas as pd


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("zomato.csv", encoding = "ISO-8859-1")
df.head()


# In[8]:


#code implementation
df.isnull()


# In[9]:


df.isnull().sum()  #give the sum of null values 


# In[10]:


df.info()


# In[13]:


df2 = df["Country Code"].fillna(value = 0)
#it will replace null values to 0
df2.head()
df2.isnull().sum()


# In[15]:


#ONE OF THE WAY TO REMOVE NULL VALUES ARE USING PAD WHICH MEANS FILLING IT WITH PREVIOUS ROWS DATA,BFIll and many more down
df3 = df.fillna(method = 'pad')
df3


# In[16]:


df4 = df.fillna(method = 'bfill')
df4


# In[18]:


plt.figure(figsize=(16, 8))  # Larger figure size

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(df['Average Cost for two'], kde=True)
plt.title('Histogram of Average Cost for two(USD)')
plt.xlim(0, 10000)

# Density Plot (KDE)
plt.subplot(1, 2, 2)
sns.kdeplot(df['Average Cost for two'], shade=True)
plt.title('Density Plot of Average Cost for two (USD)')
plt.xlim(0, 10000)

plt.tight_layout()
plt.show()


# In[19]:


df['Average Cost for two'].median()
#it gonna show the median of average cost for two


# In[22]:


#filling the null value 
df7 = df['Average Cost for two'].fillna(value = df['Average Cost for two'].median())
print(df7)


# In[23]:


# Create subplots with shared y-axis
fig, axs = plt.subplots(1, 3, figsize=(16, 6), sharey=True)  # 1 row, 3 columns

# Plot original data distribution
sns.histplot(df['Average Cost for two'], kde=True, color='lightblue', bins=40, ax=axs[0])
axs[0].set_title("Original Data Distribution")
axs[0].set_xlabel("Average Cost for two")
axs[0].set_ylabel("Frequency")
axs[0].set_xlim(0, 10000)  # Set x-axis limits for the first subplot

# Plot data distribution after filling with median
sns.histplot(df7, kde=True, color='green', bins=40, ax=axs[1])
axs[1].set_title("Data Distribution after Filling with Median")
axs[1].set_xlabel("Average Cost for two")
axs[1].set_xlim(0, 10000)  # Set x-axis limits for the second subplot

# Ensure the third subplot has the same y-axis limits as the first two
plt.xlim(0, 10000)

plt.show()


# In[24]:


df5 = df.dropna()
df5


# In[25]:


# Now let's see how does 'how' parameter work
# how='any' means if any row has a null values it is removed (default)
df11 =df.dropna(how='any')
df11


# In[26]:


df12 = df.dropna(how='all')
df12


# In[27]:


# What if you want to drop column with null values, there is a parameter for it
df13 = df.dropna(axis=1)
df13


# In[28]:


# Drop rows where specific columns have null values
df14 = df.dropna(subset=['Currency', 'City'])
df14


# In[29]:


# Drop rows with at least a certain number of non-null values
df15 =  df.dropna(thresh=5)
df15


# In[30]:


df17 = df.interpolate(method='polynomial', order=2)
df17


# In[31]:


# Interpolate missing categorical values using the most recent non-null value
df19 = df.interpolate(method='pad')
df19


# In[32]:


import numpy as np
df20 = df.replace(to_replace= np.nan, value= 0)
df20


# In[36]:


# Calculate quartiles
q1 = df['Price range'].quantile(0.25)  # First quartile (25th percentile)
q2 = df['Price range'].quantile(0.5)   # Second quartile (median)
q3 = df['Price range'].quantile(0.75)  # Third quartile (75th percentile)

print("First Quartile (Q1):", q1)
print("Median (Q2):", q2)
print("Third Quartile (Q3):", q3)

# Create a box plot to visualize skewness
sns.boxplot(x=df['Price range'])
plt.title('Box Plot for price')
plt.show() 


# In[37]:


#BEFORE
# Calculate quartiles and visualize original distribution
q1 = df['Price range'].quantile(0.25)  # First quartile (25th percentile)
q2 = df['Price range'].quantile(0.5)   # Second quartile (median)
q3 = df['Price range'].quantile(0.75)  # Third quartile (75th percentile)

print("First Quartile (Q1):", q1)
print("Median (Q2):", q2)
print("Third Quartile (Q3):", q3)

# Create a histogram to visualize original distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Price range'], bins=30, color='lightblue', edgecolor='black')
plt.axvline(x=q1, color='red', linestyle='--', label='Q1 (25th percentile)')
plt.axvline(x=q2, color='green', linestyle='--', label='Q2 (50th percentile)')
plt.axvline(x=q3, color='blue', linestyle='--', label='Q3 (75th percentile)')
plt.title('Histogram of Age - Original Distribution')
plt.xlabel('Price range')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()


# In[38]:


# Assuming df is your loan dataset loaded properly

# Select columns for KNN imputation
columns_for_knn = ['Average Cost for two', 'Price range', 'Rating text']

# Visualize histograms before imputation
plt.figure(figsize=(14, 10))
for i, col in enumerate(columns_for_knn, 1):
    plt.subplot(3, 2, i)
    plt.hist(df[col].dropna(), bins=30, color='blue', edgecolor='black')
    plt.title(f'Histogram of {col} - Before Imputation')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()


# In[40]:


# Visualize histograms before imputation (assuming df is your loan dataset)
plt.figure(figsize=(14, 10))
for i, col in enumerate(columns_for_knn, 1):
    plt.subplot(3, 2, i)
    plt.hist(df[col].dropna(), bins=30, color='blue', edgecolor='black')
    plt.title(f'Histogram of {col} - Before Imputation')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




