
# coding: utf-8

# # 随机森林建模预测

# In[2]:


import pandas as pd
import numpy as np
data= pd.read_csv("traindata3.csv")
data2=pd.read_csv("testdata2.csv")


# In[3]:


data.head()


# In[ ]:


data2.head()


# In[33]:


x_train, y_train = data.ix[:, 2:-1].values, data.ix[:, -4].values


# In[34]:


x_test, id_test = data2.ix[:, 2:].values, data2.ix[:, 1].values


# In[35]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
x_train, y_train = make_classification(n_samples=1000, n_features=33,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0,n_estimators=20)
clf.fit(x_train,y_train)
y_test=clf.predict(x_test)


# In[36]:


df = pd.DataFrame({'id': id_test,
                   'acc_now_delinq': y_test
                   
                   },columns =['id','acc_now_delinq'])
df


# In[37]:


df.to_csv("Onepiece.csv")

