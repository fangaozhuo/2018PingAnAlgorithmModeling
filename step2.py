
# coding: utf-8

# # 训练数据进一步清洗

# In[1]:


import pandas as pd
data=pd.read_csv("traindata2.csv")
data.head()


# In[2]:


data.info()


# In[3]:


#处理离散字符型变量 term,这里有坑，36 months 的前面有一个空格！
data["term"].value_counts()
term=[]
for line in data["term"]:
    if int(line[1:3]) ==36 :#36 months 的前面有一个空格，索引值从1开始
        term.append(0)
    else:
        term.append(1)
data=data.drop("term",axis=1)#删除这一列
data.insert(1,"term",term)#将列表插入这一列，不能直接用切片在原来的基础上赋值，这样会报错，必须分两步走。
# data["term"]


# In[4]:


print(data["grade"].value_counts())
grade=[]
for line in data["grade"]:
    if line =="A":
        grade.append(0)
    elif line=="B":
        grade.append(1)
    elif line=="C":
        grade.append(2)
    elif line=="D":
        grade.append(3)
    elif line=="E":
        grade.append(4)
    elif line=="F":
        grade.append(5)   
    else:
        grade.append(6)   
data=data.drop("grade",axis=1)#删除这一列
data.insert(1,"grade",grade)#将列表插入这一列，不能直接用切片在原来的基础上赋值，这样会报错，必须分两步走。
# data["grade"]


# In[5]:


data["sub_grade"].value_counts()


# In[6]:


data["emp_length"].value_counts()


# In[7]:


emp_length=[]
for line in data["emp_length"]:
    if line=="n/a":
        emp_length.append(10)
    elif line=="< 1 year":
        emp_length.append(0)
    else :
        emp_length.append(float(line[0]))
data=data.drop("emp_length",axis=1)#删除这一列
data.insert(1,"emp_length",emp_length)
# data["emp_length"]


# In[8]:


data["home_ownership"].value_counts()


# In[9]:


home_ownership=[]
for line in data["home_ownership"]:
    if line=="MORTGAGE":
        home_ownership.append(1)
    elif line=="RENT":
        home_ownership.append(2)
    elif line=="OWN":
        home_ownership.append(3)
    else:
        home_ownership.append(0)
data=data.drop("home_ownership",axis=1)
data.insert(1,"home_ownership",home_ownership)
data["home_ownership"]


# In[10]:


data["verification_status"].value_counts()


# In[11]:


verification_status=[]
for line in data["verification_status"]:
    if line=="Source Verified":
        verification_status.append(0)
    elif line=="Verified":
        verification_status.append(1)
    else:
        verification_status.append(2)
data=data.drop("verification_status",axis=1)
data.insert(1,"verification_status",verification_status)
data["verification_status"]


# In[12]:


# data["issue_d"].value_counts()
data=data.drop("issue_d",axis=1)


# In[13]:


data["loan_status"].value_counts()


# In[14]:


loan_status=[]
for line in data["loan_status"]:
    if line=="Fully Paid":
        loan_status.append(0)
    elif line=="Charged Off":
        loan_status.append(1)
    elif line=="Current":
        loan_status.append(2)
    elif line=="In Grace Period":
        loan_status.append(3)
    elif line[0:4]=="Late":
        loan_status.append(4)
    else:
        loan_status.append(5)
data=data.drop("loan_status",axis=1)
data.insert(1,"loan_status",loan_status)  
# data["loan_status"]


# In[15]:


data["pymnt_plan"].value_counts()


# In[16]:


data=data.drop("pymnt_plan",axis=1)


# In[17]:


data["purpose"].value_counts() #d待处理


# In[18]:


data["zip_code"].value_counts()


# In[19]:


data=data.drop("zip_code",axis=1)


# In[20]:


data["addr_state"].value_counts()


# In[21]:


data=data.drop("addr_state",axis=1)


# In[22]:


data["initial_list_status"].value_counts()


# In[23]:


initial_list_status=[]
for line in data["initial_list_status"]:
    if line=="f":
        initial_list_status.append(0)
    else:
        initial_list_status.append(1)
data=data.drop("initial_list_status",axis=1)
data.insert(1,"initial_list_status",initial_list_status)
# data["initial_list_status"]


# In[24]:


data=data.drop("application_type",axis=1)


# In[25]:


data.info()


# In[26]:


data["purpose"].value_counts()
data=data.drop("purpose",axis=1)


# In[27]:


data["sub_grade"].value_counts()
data=data.drop("sub_grade",axis=1)


# In[28]:


data.info()


# In[29]:


col_name = data.columns
col_name


# ### 对数据按照列进行筛选排序，没有选中的相当于删除

# In[39]:


data=data.reindex(columns=['member_id','initial_list_status', 'loan_status',
       'verification_status', 'home_ownership', 'emp_length', 'grade', 'term',
       'earliest_cr_line',  'loan_amnt', 'funded_amnt',
       'funded_amnt_inv', 'int_rate', 'installment', 'annual_inc', 'dti',
       'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'out_prncp',
       'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp',
       'total_rec_int', 'total_rec_late_fee', 'recoveries',
       'collection_recovery_fee', 'collections_12_mths_ex_med', 'policy_code', 'tot_coll_amt', 'tot_cur_bal', 'total_rev_hi_lim',
       'acc_now_delinq'])
data.head()


# In[36]:


col_name = data.columns
col_name


# In[29]:


data.head()


# In[37]:


data.to_csv("traindata3.csv" )

