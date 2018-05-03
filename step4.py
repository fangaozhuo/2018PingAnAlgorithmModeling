
# coding: utf-8

# # 利用训练数据交叉验证得到最佳模型和参数

# In[6]:


import pandas as pd
import numpy as np
data= pd.read_csv("traindata3.csv")
data.head()


# In[17]:


from sklearn.model_selection import train_test_split
x, y = data.ix[:, 2:-1].values, data.ix[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)#随机选择25%作为测试集，剩余作为训练集


# In[18]:


print(x_train.shape)
print(y_train)
print(x_test.shape)
print(y_test)


# In[19]:


x_train


# In[21]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import datetime
starttime = datetime.datetime.now()
x_train, y_train = make_classification(n_samples=1000, n_features=33,
                            n_informative=2, n_redundant=0,
                            random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0,n_estimators=20)

# clf = LogisticRegression(solver='liblinear',max_iter=10)
clf.fit(x_train,y_train)
prey_test=clf.predict(x_test)
print(clf.feature_importances_)#随机森林
tp=0
fn=0
fp=0
tn=0
for i in range(len(y_test)):
    if y_test[i]==1 and prey_test[i]==1:
        tp=tp+1
    elif y_test[i]==1 and prey_test[i]==0:
        fn=fn+1
    elif y_test[i]==0 and prey_test[i]==1:
        fp=fp+1
    else :
        tn=tn+1
def dafen(tp,fn,fp):
    r=tp/(tp+fn)
    p=tp/(tp+fp)
    f=((4+1)*p*r)/(4*p+r)
    # print("tp:",tp,"\nfn:",fn,"\nfp:",fp)
    print("f2",f)
print("tp:",tp,"\nfn:",fn,"\nfp:",fp,"\ntn:",tn)
dafen(tp,fn,fp)
endtime = datetime.datetime.now()
print(endtime-starttime)#查看程序运行了多久  

