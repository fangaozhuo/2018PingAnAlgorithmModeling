
# coding: utf-8

# # 预测数据按照训练数据的步骤进行相应的处理

# In[4]:


import pandas as pd
import datetime
starttime = datetime.datetime.now()
data = pd.read_csv("test.csv")
endtime = datetime.datetime.now()
print(endtime-starttime)#查看程序运行了多久
data.head()


# In[5]:


col_name = data.columns
col_name


# In[6]:


data.shape


# In[7]:


for item in col_name:
    freq = (data[item].notnull().sum())/177476
    if freq < 0.5:
        data=data.drop([item],axis=1)
data.head()  


# In[10]:


data.info()


# In[11]:


data["emp_title"].describe()


# In[13]:


data=data.drop(["emp_title"], axis=1)


# In[14]:


data.head()


# In[19]:


#处理连续数值型变量 annual_inc
data["annual_inc"].describe()


# In[30]:


#处理离散字符型变量 title
data["title"].describe()#贷款头衔种类太多，删除这一列。


# In[31]:


data=data.drop(["title"], axis=1)
data


# In[15]:


#处理离散字符变量 earliest_cr_line
data["earliest_cr_line"].describe()


# In[16]:


values = {'earliest_cr_line':"Aug-2001"}#按照众数最高填充空值为Aug-2001
data=data.fillna(value=values)


# In[17]:


earliest_cr_line=[]
for line in data["earliest_cr_line"]:
    earliest_cr_line.append(2018-float(line[-4:]))#先将这一列利用切片将年放进一个列表中
data=data.drop("earliest_cr_line",axis=1)#删除这一列
data.insert(1,"earliest_cr_line",earliest_cr_line)#将列表插入这一列，不能直接用切片在原来的基础上赋值，这样会报错，必须分两步走。
data["earliest_cr_line"]


# In[18]:


#处理离散变量 pub_rec
data["pub_rec"].value_counts()
#在后面统一填充众数


# In[20]:


#处理数值连续变量 revol_bal
data["revol_bal"].describe()


# In[23]:


#处理数值连续变量 revol_util
data["revol_util"].describe()
#在后面统一填中位数,查看数据可以发现循环使用率会超过100%，故最大值366应该不算是异常值


# In[21]:


#处理连续数值型变量 total_acc
data["total_acc"].describe()


# In[24]:


#处理离散数值型变量 collections_12_mths_ex_med
data["collections_12_mths_ex_med"].value_counts()


# In[25]:


#处理连续数值型变量 tot_coll_amt
data["tot_coll_amt"].describe()


# In[26]:


#处理连续离散型变量 tot_cur_bal
data["tot_cur_bal"].describe()


# In[27]:


#处理连续离散型变量 total_rev_hi_lim
data["total_rev_hi_lim"].describe()


# In[28]:


#统一对空值进行填充 
values = {"annual_inc":6.410000e+04,"pub_rec":0,"revol_bal":1.187300e+04,"revol_util":56,"total_acc": 24,"collections_12_mths_ex_med":0,          "tot_coll_amt":0,"tot_cur_bal":8.069100e+04,"total_rev_hi_lim":2.362300e+04}
data=data.fillna(value=values)


# In[32]:


data.info()
#至此空值填充完毕


# In[33]:


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


# In[35]:


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


# In[36]:


data["sub_grade"].value_counts()


# In[37]:


data["emp_length"].value_counts()


# In[38]:


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


# In[39]:


data["home_ownership"].value_counts()


# In[41]:


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
#data["home_ownership"]


# In[42]:


data["verification_status"].value_counts()


# In[43]:


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


# In[44]:


# data["issue_d"].value_counts()
data=data.drop("issue_d",axis=1)


# In[45]:


data["loan_status"].value_counts()


# In[46]:


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


# In[47]:


data["pymnt_plan"].value_counts()


# In[48]:


data=data.drop("pymnt_plan",axis=1)


# In[49]:


data["purpose"].value_counts() #d待处理


# In[50]:


data["zip_code"].value_counts()


# In[52]:


data=data.drop("zip_code",axis=1)


# In[53]:


data["addr_state"].value_counts()


# In[54]:


data=data.drop("addr_state",axis=1)


# In[55]:


data["initial_list_status"].value_counts()


# In[56]:


initial_list_status=[]
for line in data["initial_list_status"]:
    if line=="f":
        initial_list_status.append(0)
    else:
        initial_list_status.append(1)
data=data.drop("initial_list_status",axis=1)
data.insert(1,"initial_list_status",initial_list_status)
#data["initial_list_status"]


# In[58]:


data=data.drop("application_type",axis=1)


# In[60]:


data["purpose"].value_counts()
data=data.drop("purpose",axis=1)


# In[61]:


data["sub_grade"].value_counts()
data=data.drop("sub_grade",axis=1)


# In[62]:


data.info()


# In[63]:


data.head()


# In[65]:


col_name = data.columns
col_name


# In[64]:


data.to_csv("testdata2.csv")

