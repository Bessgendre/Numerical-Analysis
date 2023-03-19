#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


# Lagrange 插值算法

def LagrangeBase(x,dataX,dataY,i,n):   
    # 使用 n 次多项式插值，计算第 i 个 Lagrange 基在 x 的值
    item = 1
    for j in range(0, n+1):
        if j == i:
            continue 
        item *= (x - dataX[j]) / (dataX[i] - dataX[j])
    item *= dataY[i]
    return item

def LagrangeInterpolate(x, dataX, dataY, n):
    # 输入 n + 1 个点，
    # 使用 n 次多项式的拉格朗日插值，计算插值多项式在 x 处的值
    
    if n < len(dataX) - 1:
        print("Wrong!")
        return 0
    n = len(dataX) - 1
    result = 0
    for i in range(0, n+1):
        result += LagrangeBase(x, dataX, dataY, i, n)
    return result 


# In[55]:


# Newton 插值算法

def DifferentQuotient(dataX,dataY):
    # 给定 n+1 个点，计算 n 阶差商
    
    if len(dataX) == 1:
        return dataY[0]
    
    result = 0
    n = len(dataX) - 1
    for i in range(n + 1):
        item = 1
        
        for j in range(n + 1): # 以差商的通项公式计算 n 阶差商
            if j == i:
                continue    
            item *= 1 / (dataX[i] - dataX[j])
            
        item *= dataY[i]
        result += item
    return result  

def NewtonBase(x, dataX, dataY):
    # 计算 Newton 插值中的每一个 Newton 基在 x 处的值
    # 本函数也可用于实现承袭性，data.append 就行
    
    n = len(dataX) - 1
    result = 1
    
    if n == 0:
        return dataY[0]
    
    for i in range(n):
        result *= (x - dataX[i])
    result *= DifferentQuotient(dataX,dataY)
    
    return result

def NewtonInterpolate(x, dataX, dataY, n):
    # 输入 n + 1 个点，
    # 使用牛顿插值，计算插值多项式在 x 处的值
    result = 0
    
    for i in range(n + 1):
        result += NewtonBase(x, dataX[0:i+1], dataY[0:i+1])
    return result 


# In[ ]:


## 误差估计

def PosterioriError(x, dataX, dataY):
    # 估计后验误差，以拉格朗日形式
    
    n = len(dataX) - 2
    # 插值多项式的阶数比数据个数少 2
    
    dataX1 = dataX[0:-1]
    dataY1 = dataY[0:-1]
    dataX2 = dataX[1:]
    dataY2 = dataY[1:]
    
    error = (x - dataX[0])/(dataX[0] - dataX[n+1]) * (LagrangeInterpolate(x, dataX1,dataY1,n) - 
         LagrangeInterpolate(x, dataX2,dataY2,n))
    
    return error  


# In[9]:


# 拉格朗日插值

dataX = [11, 12]
dataY = [0.190809, 0.207912]

print(LagrangeInterpolate(11.5, dataX,dataY,1))
print(PosterioriError(11.5, dataX, dataY))


# In[13]:


dataX = [-2,2,5]
dataY = [0,3,6]

print(LagrangeInterpolate(-1.2, dataX, dataY, 2))
print(LagrangeInterpolate(1.2, dataX, dataY, 2))


# In[16]:


dataX = [81,100,121]
dataY = [9,10,11]

print(LagrangeInterpolate(105, dataX, dataY, 2))


# In[60]:


# 牛顿法插值

dataX = [-2,0,1,2]
dataY = [17,1,2,19]
print(NewtonInterpolate(0.9,dataX,dataY, 3))


# In[63]:


## 第九题

def function(x):
    return x**7 - 125 * x**5 + 237 * x**3 - 999


# In[68]:


dataX = [2**x for x in range(2)]
dataY = [function(x) for x in dataX]

print(dataX)
print(dataY)

DifferentQuotient(dataX,dataY)


# In[69]:


dataX = [2**x for x in range(8)]
dataY = [function(x) for x in dataX]

print(dataX)
print(dataY)

DifferentQuotient(dataX,dataY)


# In[70]:


dataX = [2**x for x in range(9)]
dataY = [function(x) for x in dataX]

print(dataX)
print(dataY)

DifferentQuotient(dataX,dataY)


# In[ ]:




