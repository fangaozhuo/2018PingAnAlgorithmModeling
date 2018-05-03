
# coding: utf-8

# # 训练数据空值填充

# In[5]:


import pandas as pd


# In[6]:


import datetime
starttime = datetime.datetime.now()
data = pd.read_csv("train.csv")
endtime = datetime.datetime.now()
print(endtime-starttime)#查看程序运行了多久
data.head()


# In[7]:


data.shape


# In[8]:


data.describe(include = "all")


# In[9]:


col_name = data.columns
col_name


# In[10]:


data.shape


# In[11]:


for item in col_name:
    freq = (data[item].notnull().sum())/709903
    if freq < 0.5:
        data=data.drop([item],axis=1)
data.head()  


# In[12]:


data.describe(include="all")


# In[13]:


data.info()#查看每一列不是缺失值的个数


# In[14]:


data["emp_title"].describe()


# In[15]:


data=data.drop(["emp_title"], axis=1)
data


# In[16]:


#处理连续数值型变量 annual_inc
data["annual_inc"].describe()


# In[17]:


#处理离散字符型变量 title
data["title"].describe()#贷款头衔种类太多，删除这一列。


# In[18]:


data=data.drop(["title"], axis=1)
data


# In[19]:


#处理离散字符变量 earliest_cr_line
data["earliest_cr_line"].describe()


# In[20]:


values = {'earliest_cr_line':"Aug-2001"}#按照众数最高填充空值为Aug-2001
data=data.fillna(value=values)


# In[21]:


earliest_cr_line=[]
for line in data["earliest_cr_line"]:
    earliest_cr_line.append(2018-float(line[-4:]))#先将这一列利用切片将年放进一个列表中
data=data.drop("earliest_cr_line",axis=1)#删除这一列
data.insert(1,"earliest_cr_line",earliest_cr_line)#将列表插入这一列，不能直接用切片在原来的基础上赋值，这样会报错，必须分两步走。
data["earliest_cr_line"]


# In[22]:


#处理离散变量 pub_rec
data["pub_rec"].value_counts()
#在后面统一填充众数


# In[23]:


#处理数值连续变量 revol_bal
data["revol_bal"].describe()


# In[24]:


#处理数值连续变量 revol_util
data["revol_util"].describe()
#在后面统一填中位数,查看数据可以发现循环使用率会超过100%，故最大值366应该不算是异常值


# In[25]:


#处理连续数值型变量 total_acc
data["total_acc"].describe()


# In[26]:


#处理离散数值型变量 collections_12_mths_ex_med
data["collections_12_mths_ex_med"].value_counts()


# In[27]:


#处理连续数值型变量 tot_coll_amt
data["tot_coll_amt"].describe()


# In[28]:


#处理连续离散型变量 tot_cur_bal
data["tot_cur_bal"].describe()


# In[29]:


#处理连续离散型变量 total_rev_hi_lim
data["total_rev_hi_lim"].describe()


# In[30]:


#统一对空值进行填充 
values = {"annual_inc":6.500000e+04,"pub_rec":0,"revol_bal":1.187500e+04,"revol_util":56,"total_acc": 24,"collections_12_mths_ex_med":0,          "tot_coll_amt":0,"tot_cur_bal":8.052650e+04,"total_rev_hi_lim":2.370000e+04}
data=data.fillna(value=values)


# In[31]:


data.head()


# In[32]:


data.info()
#再次查看缺失值，发现缺失值已经填充完毕


# In[37]:


data.head()


# In[35]:


#空值填完了，先保存下
data.to_csv("traindata2.csv" )

