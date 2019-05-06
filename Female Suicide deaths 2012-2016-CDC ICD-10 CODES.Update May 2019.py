
# coding: utf-8

# <h1> Project: Technology to prevent the suicides of women in the US</h1>
# <h3>Autor: Francihelena Uzcategui</h3>
# 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#cleaning">Data Cleaning</a></li>
# <li><a href="#eda">Exploratory Data Analysis </a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>
# 
# <h3>Introduction </h3>
# <p>The use of Technology to prevent the suicides of women in the US is a project connected to the Hackathon event at Data Science Scholarship Program Powered by Bertelsmann and Udacity. </p>
# <p>First, we performed an exploratory analysis of raw data from the Center for Disease control and prevention. Further, we investigated three methods that use technology tools to prevent female suicide. As a conclusion, we consider that technology brings important ways to suicide’s prevention. </p>
# <p>The Education Pioneers datasets have univariate and bivariate data to analyze — relations between Education and Demographic indexes, and how they affect the growth and development of students. </p>
# 
# <h5>Questions </h5>
#     
# <h6>1- What are the causes of Deaths among the women between 2012-2016?</h6> 
#    
# <h6>2- How many Female Suicide deaths occurred between 2012-2016?</h6>
# 
# <h6>3- What is the distribution of Female suicides deaths by Age-Groups?</h6>
# 
# <h6>5- How is the Female suicides deaths by states 2012-2016?</h6>

# <h3>Data Wrangling</h3>

# In[1]:


import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("C:/Users/Franchi/Documents/Project Technology to prevent Women's suicide in U.S/Underlying Cause of Death, 1999-2016 WITH AGES.txt",delimiter = "\t")


# In[3]:


data #MUST call the data if not any results will show


# <h3>Data Cleaning</h3>

# In[4]:


data.isnull().sum(axis = 0)


# <h3>Exploratory Data Analysis</h3>

# In[5]:


#1) Female's suicide by Cause of death according to ICD-10 codes: X60,X71,X72,X74,X75,X84,Y87.0


# In[6]:


data.groupby('Cause of death Code').Deaths.count()


# In[7]:


#10 Codes: X60 (Intentional self-poisoning by and exposure to nonopioid analgesics, antipyretics and antirheumatics), X71"
#"(Intentional self-harm by drowning and submersion), X72 (Intentional self-harm by handgun discharge), X74 (Intentional self-harm"
#"by other and unspecified firearm discharge), X75 (Intentional self-harm by explosive material), X84 (Intentional self-harm by"
#"unspecified means), Y87.0 (Sequelae of intentional self-harm)" 
#https://www.cdc.gov/nchs/data/datalinkage/underlying_and_multiple_cause_of_death_codes.pdf


# In[8]:


sum(pd.isnull(data['Cause of death']))


# In[9]:


Total_cause_of_death_num=[19,168,387,389]
Total_cause_of_death_name=['Intentional self-harm by drowning and submersion', 'Intentional self-harm by handgun discharge','Intentional self-harm by other and unspecified firearm discharge', 'Diverse causes Intentional self-harm']


# In[10]:


plt.figure(figsize=(18,8))
plt.pie(Total_cause_of_death_num,  autopct='%0.1f%%')
plt.axis('equal')
plt.legend(Total_cause_of_death_name, loc=4)
plt.title("Female's Suicide Cause of Deaths, 2012-2016. N=963")
plt.savefig("C:/Users/Franchi/Documents/Project Technology to prevent Women's suicide in U.S/my_pie_chart-Female's Suicide Cause of Death.png")
plt.show()


# In[11]:


#2) Female's Suicide Deaths by Year


# In[12]:


data.groupby('Year').Deaths.mean()


# In[13]:


data.groupby('Year').Deaths.mean().plot(kind='bar')
plt.title("Female's Suicide deaths by years 2012-2016")


# In[14]:


#3) Female's suicides deaths by Age-Groups


# In[15]:


data.groupby('Five-Year Age Groups').Deaths.mean()


# In[16]:


data.groupby('Five-Year Age Groups').Deaths.mean().plot(kind='bar')
plt.title("Female's suicides deaths by Age-Groups 2012-2016")


# In[17]:


#Female's suicides deaths by states 2012-2016 - Graph in Tableau: https://public.tableau.com/views/Femalessuicidesdeathsbystates2012-2016/Sheet2?:embed=y&:display_count=yes


# In[18]:


data.groupby('State').Deaths.mean()


# 
# 
# ![](Documents/Project Technology to prevent Women's suicide in U.S/mapa1.JPG?raw=true)
# 

# <h3>Conclusions</h3>
# 
# <p>Suicide is the 10th leading cause of death in the US; it is a public health issue. The suicide rates are increasing among the women.</p> 
