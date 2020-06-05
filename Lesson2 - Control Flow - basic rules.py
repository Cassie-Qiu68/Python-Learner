#!/usr/bin/env python
# coding: utf-8

# In[6]:


###if, elif and else###

###语句示例
# if x < 0:
#     print('it\'s negt')
# elif x == 0:
#     print('Equal to zero')
# elif 0 < x < 5:
#     print('Positive but smaller than 5')
# else:
#     print('Positive and larger than or equal to 5')

a = 5; b = 7
c = 8; d=4
if a < b or c>d:
    print('Made it')


# In[15]:


### for ###

#for 用于遍历一个集合（eg.列表或元组）或一个迭代器。
#对非None值进行累加
# s = [1, 2, None, 4, None, 5]
# total = 0
# for value in s:
#     if s is None:
#         continue     #continue用于跳过continue 后面的代码进入下一次循环
#     total += value

#对列表进行累加，直到5出现
s = [1,2,0,4,6,5,2,1]
total_util_5 = 0
for value in s:
    if value == 5:
        break         #break 结束for循环
    total_util_5 += value 
total_util_5

##continue 是跳过；break是结束循环


# In[16]:


for i in range(4):
    for j in range(4):
        if j > i :
            break   #此时只会停止内循环，不会停止外循环
            
        print((i,j))
        


# In[18]:


### while ###
x = 256
total =0
while x > 0:
    if total > 500:
        break      #while 会在符合条件的情况下一直执行代码块，知道判断条件为false 或 break结尾时 才结束
    total += x
    x = x // 2
x


# In[19]:


### pass ###
input(x)
if x < 0:
    print('negative!')
elif x == 0:
    #一个占位
    pass ##什么都不做
else:
    print("positive!")


# In[20]:


### range ###
#range函数返回一个迭代器，生成一个等差整数序列
list(range(10))


# In[21]:


list(range(0,10,2)) #包含起始不包含结尾


# In[23]:


list(range(5,0,-1)) ###步长可以是负数


# In[27]:


seq = [1,2,3,4]
for i in range(len(seq)):  #根据序列的索引遍历序列
    val = seq[i]
val


# In[28]:


### 三元表达方式 ###
x = 5
'non-negavtive' if x > 5 else 'Negative'

