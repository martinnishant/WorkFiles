#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# In[27]:


df = pd.read_csv("zomato.csv", encoding = "ISO-8859-1")


# In[28]:


df.head()


# In[29]:


df.shape


# In[30]:


df.describe()


# In[31]:


df.info()


# In[32]:


null_values = df.isnull().sum()


# In[33]:


print(null_values)


# In[ ]:





# In[34]:


df=df.drop("Locality Verbose", axis=1)


# In[35]:


df.shape


# In[36]:


df=df.drop("Locality", axis=1)


# In[37]:


df.shape


# In[38]:


df['Cuisines'].unique()


# In[39]:


df['Cuisines'].nunique()


# In[40]:


df['Cuisines']=df['Cuisines'].fillna("No Cuisines")


# In[41]:


null_values = df.isnull().sum()


# In[42]:


print(null_values)


# In[43]:


from sklearn.tree import DecisionTreeRegressor


# In[45]:


df['City'].unique()


# In[46]:


df['City'].nunique()


# In[51]:


sns.boxplot(x=df['Price range'])


# In[52]:


sns.countplot(x = 'Has Table booking', data = df)


# In[54]:


sns.countplot(x="Has Online delivery", data = df)


# In[55]:


sns.barplot(x=df['Rating text'], y = df["Votes"], hue=df['Rating color'])


# In[57]:


df.groupby("Rating color").mean(numeric_only = True)["Votes"]


# In[61]:


plt.rcParams['figure.figsize'] = (13, 9)
Y = pd.crosstab(df['Aggregate rating'], df['Has Table booking'])
Y.div(Y.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True,color=['red','yellow'])
plt.title('table booking vs rate', fontweight = 30, fontsize = 20)
plt.legend(loc="upper right")
plt.show()


# In[ ]:


sns.countplot(df['City'])
sns.countplot(df['City']).set_xticklabels(sns.countplot(df['City']).get_xticklabels(), rotation=90, ha="right")
fig = plt.gcf()
fig.set_size_inches(13,13)
plt.title('Location')

