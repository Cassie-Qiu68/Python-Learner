#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = 'python' #字符串可以是单引号或双引号
a = list(s)
b = a[:3] 
c = s[:3] #注意b和c的类型差异，list和str


# In[6]:


s = '12\\34' #  \ 是转义字符
print(s)    #print() 以及和直接s的区别


# In[9]:


s = r'this\ is\ a \test' #前面加r代表每一个\都是两个\\
s


# In[10]:


a = 'hello'
b = 'world'
a + b       #字符串合并


# In[11]:


#字符串格式化
template = '{0:.2f}{1:s} are worth US${2:d}'
#{0:.2f} 表示第一个参数格式化为 2位浮点小数的浮点数
#{1:s} 表示第二个参数格式化位字符串
#{2:d} 表示第三个参数格式化为整数
template.format(4.5560,'Argentine Pesos',1)


# In[16]:


#日期和时间
#内建datetime模块
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30 ,21)
dt.day
dt.date()


# In[18]:


#datetime转换为字符串，strftime
dt.strftime('%m/%d/%Y %H:%M')


# In[19]:


#字符串转为datetime对象,strptime
datetime.strptime('20091031','%Y%m%d')


# In[20]:


#替换
dt.replace(minute = 0,second = 0)
#datetime是不可变类型，以上方法是产生新的对象

