#!/usr/bin/env python
# coding: utf-8

# # IBM Web Scrapping

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "http://www.ibm.com"


# In[3]:


data  = requests.get(url).text 


# In[4]:


soup = BeautifulSoup(data,"html5lib")


# In[5]:


for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# In[6]:


for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# # Scarpping data from Html tables

# In[7]:


#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# In[8]:


# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text


# In[9]:


soup = BeautifulSoup(data,"html5lib")


# In[10]:


#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>


# In[11]:


#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].text # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

