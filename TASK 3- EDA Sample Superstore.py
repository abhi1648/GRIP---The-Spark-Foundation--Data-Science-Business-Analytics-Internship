import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


SampleSuperstore_data=pd.read_csv("Downloads\SampleSuperstore.csv")


# In[4]:


SampleSuperstore_data.head()


# In[5]:


SampleSuperstore_data.info()


# #### So, from the info fuction we can see that there are 9994 entries and 9994 non-null count for each columns which means no missing value is present. So now let us chechk the duplicate entries.

# In[6]:


SampleSuperstore_data.duplicated().sum()


# ## So, there are 17 duplicate entries and let us drop them.

# In[7]:


SampleSuperstore_data.drop_duplicates(inplace= True)


# In[8]:


SampleSuperstore_data.info()


# ## Let us now drop the unnecessary columns 

# In[9]:


SampleSuperstore_data.drop(["Postal Code"], axis=1,inplace= True)


# In[11]:


SampleSuperstore_data.info()


# ## Let us see the correlation between the numerical columns 

# In[12]:


SampleSuperstore_data.corr()


# In[15]:


sns.heatmap(SampleSuperstore_data.corr(), annot=True)


# ## Let us see the different kind of Ship Modes, Segments and categories

# In[16]:


SampleSuperstore_data["Ship Mode"].value_counts()


# In[25]:


sns.countplot(x= SampleSuperstore_data['Ship Mode'])


# In[26]:


SampleSuperstore_data["Segment"].value_counts()


# In[27]:


sns.countplot(x= SampleSuperstore_data['Segment'])


# In[28]:


SampleSuperstore_data["Category"].value_counts()


# In[29]:


sns.countplot(x= SampleSuperstore_data['Category'])


# ## Concluding that Office Supplies Category consists Highest Number. Now let us see the sub-categories as well.

# In[30]:


SampleSuperstore_data["Sub-Category"].value_counts()


# In[38]:


plt.figure(figsize=(10,10))
plt.pie(SampleSuperstore_data["Sub-Category"].value_counts(), labels= SampleSuperstore_data["Sub-Category"].value_counts().index, autopct ="%2f")
plt.show()


# ## Here, highest Sub-Category is Binder, follwed by Paper and Furnishing as Second and Third respectively.

# In[39]:


st_profit=SampleSuperstore_data.groupby(["State"])["Profit"].sum().nlargest(20)


# In[40]:


st_profit


# In[53]:


plt.figure(figsize=(20,20))
st_profit.plot.bar()


# In[58]:


sns.lineplot(data=SampleSuperstore_data, x="Discount", y= "Profit")


# ## So, as discount rises clearly profit falls. 

# In[77]:


SampleSuperstore_data.plot(kind="scatter",x="Sales",y="Profit", c="Discount", colormap="Set1",figsize=(10,10))


# ## From this scatterplot we can cxlearly say that more  sale does not mean more profit. It depends on discount as well. Where Sales is high along with low discount, profit margin is higher. 

# In[80]:


data1= SampleSuperstore_data.groupby("State")[["Sales","Profit"]].sum().sort_values(by="Sales", ascending=False)
data1[:].plot.bar(color = ["Green","Red"], figsize=(20,15))
plt.title("Profit-Loss and Sales across States")
plt.show()


# ## We can say that attention should be given to California, NewYork as they generate more profit compared to others. We can see this region wise as well.

# In[82]:


data1= SampleSuperstore_data.groupby("Region")[["Sales","Profit"]].sum().sort_values(by="Sales", ascending=False)
data1[:].plot.bar(color = ["Black","Blue"], figsize=(10,7))
plt.title("Profit-Loss and Sales across Region")
plt.show()


# # Conclusion:
# ###  1. Western Region generates highest profit.
# ###  2. Focus should be given to Calefornia, NewYork, Washington. 
# ###  3. The Central region generates lowest profit. 
# ###  4. Texas, Pennsylvenia, Florida, Ohio and some other states are generating loss with high sale. So we need to give attention towards them.
# 
# ##  Therefore, we have to work more on California and NewYork. Increse the sales in these states by reducing sales in states like Texas, Florida, Ohio. Decrese discount in Central region to increse profit and finaly increase the sale of Office Supplies category as they contribute more.
# 
# 

# In[ ]:
