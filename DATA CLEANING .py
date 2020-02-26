
# coding: utf-8

# __NOTE:__
# 
# 1) This document is arranged in an order following the __Case_description__
# 
# 2) Section A OVERVIEW is available in the __Case_description__
# 
# 3) This document starts from SECTION B  DATA PREPARATION as per __Case_desription__ 
# 

# In[1]:


#Import libraries 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# # SECTION B     DATA PREPARATION
# ##  B.2         Data pre-processing

# ### B.2.1   Item Data 

# In[2]:


#read in items data
items = pd.read_csv('Item.csv', sep = ',')


# In[3]:


items.info()


# In[4]:


items.PURCHASEPRICE.isnull().any()


# #### Data-type contraints: cleaning, verifying and reporting

# In[5]:


# Change dtype of saleprice to decimal 
before = type(items.SALEPRICE[0])
items.SALEPRICE = items.SALEPRICE.astype('float64')
after = type(items.SALEPRICE[0])
before
after


# In[6]:


# check the size of the dataframe 
items.shape


# In[7]:


# check the first 5 rows of the items dataframe 
items.head()


# In[8]:


# check data types of the columns based on the data dictionary 
items.info()


# ##### Reporting: As seen above, the currently stored items data type meets the data-type contraints requirments. 

# ### B.2.2    Customer Data 

# In[9]:


#read in customer data
customers = pd.read_csv('CustomerData.txt', sep='|')
customers


# In[10]:


#check dtypes 
customers.info()


# #### Data-type contraints: cleaning, verifying and reporting

# In[11]:


#change "DOB" field to date dtype

customers['DOB']= pd.to_datetime(customers['DOB']) 


# In[12]:


#check dtype again
customers.info()


# ##### Reporting: As seen above, the currently stored customers data type meets the data-type contraints requirments.

# In[13]:


# save a copy of the currently stored data in .csv file. 
customers_prep = pd.DataFrame(customers)
customers_prep.to_csv('customers_prep.csv')
customers_prep.to_csv(r'C:\Users\YUJI6004\customers_prep.csv', index=False)


# ### B.2.3  Transaction Data 

# In[14]:


#read in transaction data 
transactions = pd.read_csv('TransactionsData.txt', sep='|', low_memory=False)
transactions


# #### Data-type contraints: cleaning, verifying and reporting

# In[15]:


# check the raw data type and compare with data dictionary 
transactions.info()


# #### Correct the following datatypes in transactions DB: 
# Rating(int64),TIMESTAMP(Time), UserID (int64 ), QTY(int64), Discount (int64),  SHIPDAYS(int64), DELIVERYDATE (Date),  TRACKNO(int64)

# #### 1) Change "RATING" from object to int64

# In[16]:


#Check unique values in RATING 
transactions.RATING.unique()


# In[17]:


# replace ' ' with 0 in RATING field 
transactions['RATING'].replace(to_replace = ' ',value ="0", inplace=True) 


# In[18]:


# Re-check unique values in RATING after replacement 
transactions['RATING'].unique()


# In[19]:


# change data type 
transactions['RATING'] = transactions['RATING'].astype('int64')


# In[20]:


# check datatype 
transactions.info()


# #### 2) Change "TIMESTAMP" from object to timestamp

# In[21]:


# check unique values in TIMESTAMP 
transactions['TIMESTAMP'].unique()


# In[22]:


#replace unknown timestamp (' ') with "00:00:00"
transactions['TIMESTAMP'].replace(to_replace = ' ',value ="00:00:00", inplace=True) 


# In[23]:


# re-check unique values in TIMESTAMP
transactions['TIMESTAMP'].unique()


# In[24]:


transactions['TIMESTAMP'] = pd.to_timedelta(transactions['TIMESTAMP'])


# In[25]:


transactions.info()


# In[26]:


transactions.TIMESTAMP.unique()


# #### 3) Change "USERID" from object to int64

# In[27]:


transactions.USERID.unique()


# In[28]:


transactions.USERID.max()


# In[29]:


#replace unknown USERID (' ') with "99999"
transactions['USERID'].replace(to_replace = ' ',value ='50000', inplace = True) 


# In[30]:


transactions.USERID = transactions.USERID.astype('int64')


# In[31]:


transactions.USERID.dtype


# #### 4) Change "QTY" from object to int64

# In[32]:


transactions.QTY = transactions.USERID.astype('int64')


# In[33]:


transactions.info()


# #### 5) Change "DISCOUNT" from object to int64

# In[34]:


transactions.DISCOUNT.unique()


# In[35]:


transactions.DISCOUNT.replace(to_replace = ' ',value ='00', inplace = True) 


# In[36]:


transactions.DISCOUNT.unique()


# In[37]:


transactions.DISCOUNT = transactions.DISCOUNT.astype('int64')


# In[38]:


transactions.info()


# #### 6) Change "SHIPDAYS " from object to int64

# In[39]:


transactions.SHIPDAYS.unique() 


# In[40]:


transactions.SHIPDAYS.replace(to_replace = ' ',value ='00', inplace = True) 


# In[41]:


transactions.SHIPDAYS = transactions.SHIPDAYS.astype('int64')


# In[42]:


transactions.SHIPDAYS.dtype


# In[43]:


transactions.SHIPDAYS.unique()


# In[44]:


transactions.info()


# #### 7) Change "DELIVERYDATE " from object to date

# In[45]:


transactions['DELIVERYDATE'].unique()


# In[46]:


transactions.DELIVERYDATE.replace(to_replace = ' ',value ='2019-12-30', inplace = True) 


# In[47]:


transactions['DELIVERYDATE'].unique()


# In[48]:


transactions['DELIVERYDATE']= pd.to_datetime(transactions['DELIVERYDATE']) 


# In[49]:


transactions.info()


# In[50]:


transactions.head()


# #### 8) Change "TRACKNO" from object to int64

# In[51]:


transactions.TRACKNO.unique()


# In[52]:


transactions.TRACKNO.max()


# In[53]:


transactions.TRACKNO.replace(to_replace = '3e+05',value ='300000', inplace = True) 
transactions.TRACKNO.replace(to_replace = '4e+05',value ='400000', inplace = True) 
transactions.TRACKNO.replace(to_replace = ' ',value ='500000', inplace = True) 


# In[54]:


transactions.TRACKNO = transactions.TRACKNO.astype('int64')


# #### Validate date types and data display 

# In[55]:


transactions.info()


# In[56]:


transactions.head()


# ##### Reporting: As seen above, the currently stored transactions data type meets the data-type contraints requirments.

# In[57]:


# save a copy of the currently stored transaction database as .csv
transactions_prep = pd.DataFrame(transactions)
transactions_prep.to_csv('transactions_prep.csv')
transactions_prep.to_csv(r'C:\Users\YUJI6004\transactions_prep.csv', index=False)


# ## B.3   Data Cleaning

# ### B.3.1  Data Quality 
# #### Items Data

# #### 1) Check for duplicated rows

# In[58]:


items.duplicated(['ITEM', 'CATEGORY', 'COLOR', 'SUPLID', 'PURCHASEPRICE', 'SALEPRICE']).value_counts()


# In[59]:


items.duplicated(['ITEM', 'CATEGORY', 'COLOR', 'SUPLID', 'PURCHASEPRICE', 'SALEPRICE']).value_counts()*100/len(items)


# #### Reporting: as seen above, almost 87% of data are duplicates across all fields. We need to remove duplicates. 

# In[60]:


# drop duplicates 
items.drop_duplicates(inplace=True)


# In[61]:


# verify if duplicates are dropped 
items.duplicated(['ITEM', 'CATEGORY', 'COLOR', 'SUPLID', 'PURCHASEPRICE', 'SALEPRICE']).value_counts()


# #### 1) Check Range Constraints: ITEM, CATEGORY, COLOR

# In[62]:


# Let's start with quantitative variables 
items.describe()


# In[63]:


items.ITEM.nunique()


# ##### As seen above, item is within [100000, 500000] range. 

# In[64]:


# display disctinct value in COLOR
items.COLOR.unique()


# In[65]:


# display unique values in CATEGORY
items.CATEGORY.unique()


# ##### As seen above, COLOR and CATEGORY are within the Length requirements. 

# #### 2) Check Unique Constraints, missing values and determine primary /composite keys

# In[66]:


# count distinct values in ITEM field 
items.ITEM.nunique()


# #### Reporting: As seen above, ITEM field is not a primary key. In fact, ITEM field could be a foreign key to TransactionDB; COLOR and CATEGORY is distinct to each ITEM code. 

# In[67]:


# number of COLOR
items.COLOR.value_counts().count()


# In[68]:


# number of categories 
items.CATEGORY.value_counts().count()


# #### Determining primary key or composite key field(s)

# In[69]:


# find number of distinct SUPLID
items.SUPLID.nunique()


# #### check missing values

# In[70]:


items.notnull().sum()


# In[71]:


print('' in items['SUPLID'])


# In[72]:


print('null' in items['SUPLID'])


# In[73]:


# Check counts of missing values
items.isnull().sum()*100/len(items)


# #### Reporting: As seen above, there are 3.84% of missing data in SUPLID. 

# In[74]:


# count the number of missing values in PURCHASEPRICE
items[items.PURCHASEPRICE == 0.0].count()


# In[75]:


# count the % of missing values in PURCHASEPRICE
items[items.PURCHASEPRICE == 0.0].count()*100/len(items)


# #### As seen above, there are 0.009 % of missing PURCHASEPRICE (n=200) 

# In[76]:


items[items.PURCHASEPRICE == 0.0].groupby(['SALEPRICE']).count()


# #### As seen above, there are 0.009 % of missing SALEPRICE (n=200) 

# #### Reporting: 1)  ITEM is a foreign Key. Each item refers to distinct COLOR and CATEGORY. The same ITEM can have multiple SUPLID.  2) No missing values except those in SUPLID field. 

# In[78]:


#### Save a copy of items pre-processed data 
items_prep = pd.DataFrame(items)
items_prep.to_csv('items_prep.csv')
items_prep.to_csv(r'C:\Users\YUJI6004\items_prep.csv', index=False)
# load the saved copy and verify dtypes consistency 
items_prep = pd.read_csv('items_prep.csv', sep =',')
items_prep.info()


# ### Decompose ITEMDB

# In[79]:


supls = pd.DataFrame(items_prep, columns = ['SUPLID', 'PURCHASEPRICE', 'ITEM' ])
supls.head()


# In[80]:


supls.info()


# In[81]:


supls.SUPLID.unique()


# In[82]:


supls.isnull().sum()


# In[83]:


supls.SUPLID.value_counts()


# In[84]:


supls.info()


# In[85]:


supls.SUPLID[supls.SUPLID==' '].count()


# In[86]:


#### Save a copy of items pre-processed data 
items_prep = pd.DataFrame(items)
items_prep.to_csv('items_prep.csv')
items_prep.to_csv(r'C:\Users\YUJI6004\items_prep.csv', index=False)
# load the saved copy and verify dtypes consistency 
items_prep = pd.read_csv('items_prep.csv', sep =',')
items_prep.info()


# ### Customers dataset
# 
# #### 1) Check range constraints of USERID and GENDER fields

# In[87]:


#check statistics of quantitative variable 
customers.describe()


# In[88]:


# check data integrity of GENDER.
customers.GENDER.unique()


# #### Reporting: As seen above, USERID is within the required range [10000, 50000]. GENDER field meets with data constraints: [F, M,N]

# #### 2) Check Primary/Foreign keys

# In[ ]:


#count the distinct number of USERID
customers.USERID.nunique()


# 
# #### Reporting: As seen above, the count of total rows is the same as the number of unique values in USERIDs (=574). Thus, USERID is the primary key 

# #### 3) Check missing values

# In[89]:


# check missing values in customers DB
customers.isna().any()


# In[90]:


# count the number each GENDER 
customers.GENDER.value_counts()


# #### As seen above, no missing values in the customer DB. However, it is worth mentiong that the GENDER field has 56 N USERIDs. Those are the USERs without gender info, perhaps their gender identity is not disclosed or considered as transgender, or representing other minor sexualities  etc. 

# In[91]:


# check unique values in COUNTRY
customers.COUNTRY.unique()


# #### Reporting: as shown above, no missing values in COUNTRY

# In[92]:


# check unique values in EDUCATION
customers.EDUCATION.unique()


# In[93]:


customers.EDUCATION.value_counts(ascending=True)


# In[94]:


customers.EDUCATION.value_counts(normalize=True)


# ##### As seen above, 19.16% of Education data is missing 
# 
# #### It is worth mentioning that ' ' is stored as a string, thus the isnull() function is evaluated as false.

# In[95]:


# replace ' ' with Null in EDUCATION
customers.EDUCATION = customers.EDUCATION.replace(to_replace = ' ', value = 'Null')


# In[96]:


# Verify the replacement 
customers.EDUCATION.unique()


# In[97]:


# check unique values in HOBBY
customers.HOBBY.unique()


# In[98]:


# check number of missing values in HOBBY
customers.HOBBY.value_counts(ascending=True)


# In[99]:


# replace ' ' with Null in HOBBY
customers.HOBBY = customers.HOBBY.replace(to_replace = ' ', value = 'Null')


# In[100]:


# Verify the replacement 
customers.EDUCATION.unique()


# In[101]:


# check % of missing values in HOBBY
customers.HOBBY.value_counts(normalize=True)


# In[102]:


customers.sort_values('DOB',ascending = True)


# ##### Transactions dataset

# In[103]:


transactions.head()


# #### To start with, let's look at the quantitative variables 

# In[104]:


#check statistics of quantitative variable 
transactions.describe()


# #### As seen above, the summary statistics of USERID and QTY is identical!! Thus, QTY is not a reliable field. 

# In[105]:


# count the number of distinct values in USERID
transactions.USERID.nunique()


# In[106]:


# count the number of distinct values in ITEM
transactions.ITEM.nunique()


# In[107]:


# count the number of distinct values in QTY
transactions.QTY.nunique()


# In[108]:


transactions.sort_values('QTY', axis=0, ascending = True, na_position ='first')


# In[109]:


transactions[transactions.QTY == 0].count()


# In[110]:


# Number count of distinct values in RATING 
transactions.RATING.value_counts()


# In[111]:


transactions.RATING.value_counts(normalize = True)


# #### As seen above, 25.98% of data missing in RATING

# In[112]:


# Checking null values in dataframe 
transactions.isnull().any()


# In[113]:


#value count by % in TIMESTAMP
transactions['TIMESTAMP'].value_counts(normalize=True)


# ##### As shown above, TIMESTAMP hour is within [00, 24].

# #### Let's look at the categorical values in transactions DB

# In[114]:


transactions.info()


# In[115]:


transactions.PAYMENT.value_counts()


# In[116]:


transactions.PAYMENT.value_counts()*100/len(transactions)


# #### As shown, 20% of missing data in PAYMENT

# In[117]:


transactions.WAREHOUSE.unique()


# In[118]:


transactions.WAREHOUSE.value_counts()


# In[119]:


transactions.WAREHOUSE.value_counts()*100/len(transactions)


# ##### As seen above, 16.65% of WAREHOUSE data is missing (n=364427)

# In[120]:


#value count TIMESTAMP (order=ascending)
transactions['TIMESTAMP'].value_counts(ascending=True)


# In[121]:


transactions.WEBBROWSER.unique()


# In[122]:


transactions['WEBBROWSER'].value_counts(normalize = True)


# In[123]:


transactions['WEBBROWSER'].value_counts(ascending = True)


# #### As displayed, 0.0668 % of missing data (n=146192) in WEBBROWSER.

# In[124]:


transactions['REVIEW'].value_counts(ascending = True)


# In[125]:


transactions['REVIEW'].value_counts(normalize = True)


# ##### As shown above, 10% of missing data in REVIEW (n=219,272)

# In[126]:


transactions.PPC_ADD.value_counts()


# In[127]:


transactions.PPC_ADD.value_counts()*100/len(transactions)


# #### As shown, 0.7% of missing data in PPC_ADD

# In[128]:


transactions.PURCHASE.value_counts()


# In[129]:


transactions.PURCHASE.value_counts()*100/len(transactions)


# #### As seen above, 10% of missing data in PURCHASE (n=218913)

# In[130]:


list(transactions.columns.values)


# In[131]:


# check duplicates
transactions.duplicated(['USERID',
 'WEBBROWSER',
 'PPC_ADD',
 'ITEM',
 'PURCHASE',
 'DISCOUNT',
 'PAYMENT',
 'WAREHOUSE',
 'SHIPDAYS',
 'DELIVERYDATE',
 'REVIEW',
 'RATING',
 'TRACKNO',
 'TIMESTAMP']).value_counts()* 100/len(transactions)

