#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('load_ext', 'sql')

import pandas as pd
import csv, sqlite3

con = sqlite3.connect("FinalDB.db")
cur = con.cursor()


# In[ ]:


#Contains links to 3 different datasets which are saved within the database.


# In[ ]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
df.to_sql("CENSUS_DATA", con, if_exists='replace', index = False, method = "multi")

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS", con, if_exists='replace', index = False, method = "multi")

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
df.to_sql("CHICAGO_CRIME_DATA", con, if_exists='replace', index = False, method = "multi")


# In[ ]:


#This now establishes a connection between SQL magic and the database.


# In[ ]:


get_ipython().run_line_magic('sql', 'sqlite:///FinalDB.db')


# In[ ]:


#This uses a sub-query to determing the community area name with the most number of crimes.

get_ipython().run_line_magic('sql', 'SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE COMMUNITY_AREA_NUMBER IN (SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(COMMUNITY_AREA_NUMBER) DESC LIMIT 1);')


# In[ ]:


#This finds the total number of crimes recorded in the CRIME table.

get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM CHICAGO_CRIME_DATA;')


# In[ ]:


#This lists the community area names and numbers with per capita income less than 11000.

get_ipython().run_line_magic('sql', 'SELECT COMMUNITY_AREA_NAME, PER_CAPITA_INCOME FROM CENSUS_DATA WHERE PER_CAPITA_INCOME < 11000;')


# In[ ]:


#This lists all case numbers for crimes involving minors.

get_ipython().run_line_magic('sql', "SELECT CASE_NUMBER, DESCRIPTION FROM CHICAGO_CRIME_DATA WHERE DESCRIPTION LIKE '%MINOR%';")


# In[ ]:


#This lists all kidnapping crimes involving a child.

get_ipython().run_line_magic('sql', "SELECT CASE_NUMBER, PRIMARY_TYPE, DESCRIPTION FROM CHICAGO_CRIME_DATA WHERE PRIMARY_TYPE LIKE '%KIDNAP%' AND DESCRIPTION LIKE '%CHILD%';")


# In[ ]:


#This lists all crimes that were recorded at schools

get_ipython().run_line_magic('sql', "SELECT DISTINCT(PRIMARY_TYPE), LOCATION_DESCRIPTION FROM CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION LIKE 'SCHOOL%';")


# In[ ]:


#This lists the types of schools along with the average safety score for each type.

get_ipython().run_line_magic('sql', 'SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS GROUP BY "Elementary, Middle, or High School";')


# In[ ]:


#This lists the 5 community areas with the highest % of households below the poverty line.

get_ipython().run_line_magic('sql', 'SELECT COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM CENSUS_DATA ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC limit 5;')

