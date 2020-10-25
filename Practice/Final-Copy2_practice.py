#!/usr/bin/env python
# coding: utf-8

# In[1]:
#%%

# Import the requests library.
import requests
import numpy as np
import pandas as pd
# Import the requests library.
import requests
import datetime
from datetime import datetime
# import matplotlib.pyplot as plt
# Dependencies for the wine API
import urllib
import json
# Import the API key.
# from config import weather_api_key
import calendar

Token = 'tylRGHbxqiZUDNymMowCBFCuEqeULiWk'
Token_NOAA=Token
API_Token='Token d8f94b93417333267ca0edcca7dc14a9e035e1bb'


# In[2]:


# https://github.com/crvaden/NOAA_API_v2
# https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859
# https://cran.r-project.org/web/packages/rnoaa/rnoaa.pdf
# file:///C:/Users/15124/Downloads/GHCND_documentation.pdf
# https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt


# # For Loop with several zip codes
# 

# In[40]:


# Create empty lists to append the data into
dates_temp = []
temps = []
dates_prcp = []
prcp = []
temps_MAX=[]
temps_MIN=[]
dates_temp_MAX=[]
dates_temp_MIN=[]
# zip_codes=[97218,99336]
zip_codes=[97218]

names=['avgTemp_WA', 'avgTemp_CA']
# names=['avgTemp_WW']
 # #initialize dataframe
df_temp_MAX = pd.DataFrame()
df_temp_MIN = pd.DataFrame()
df_temp_AVG = pd.DataFrame()
df_temp_combined=pd.DataFrame()
bigdf=pd.DataFrame()

#%%

# for i,name in zip(range(len(zip_codes)), names):
# zip_=zip_codes[i]
#Identify what years we want Temp and Prcp data for
# for year in range(2010, 2011):
# year = str(year)
#Print out 'working on year' to idenfity if script is running correctly
# print('working on year '+year)
#make the api call for temp and precipitation
r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:97218&datatypeid=TMAX&datatypeid=TMIN&units=standard&limit=1000&startdate=2010-01-01&enddate=2010-12-31', headers={'token':Token})


#%%
#Load JSON data
d = json.loads(r.text)
#         print(d)
#         df = pd.DataFrame.from_dict(d, orient='columns')

#e = json.loads(p.text)
avg_temps_MAX = [item for item in d['results'] if item['datatype']=='TMAX']
# print(avg_temps_MAX)
#%%

#get the date field from all average temperature readings
dates_temp_MAX += [item['date'] for item in avg_temps_MAX]

#%%
df=pd.DataFrame(dates_temp_MAX)
df=df.apply(pd.to_datetime)
df.dtypes

#get the actual average temperature from all average temperature readings
temps_MAX += [item['value'] for item in avg_temps_MAX]

#%%
# #populate date and average temperature fields (cast string date to datetime
df_temp_MAX['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp_MAX]
# dates_temp_MAX['date'].apply(pd.to_datetime)
#%%
type(dates_temp_MAX[0]['date'])
#%%
print(dates_temp_MAX)
# Create a column for max temps
df_temp_MAX['avgTemp'] = temps_MAX

#%%

#convert daily summaries to monthly data
df_temp_MAX = df_temp_MAX.set_index('date').resample('M').mean()
        
#         df_temp_MAX.reset_index(inplace=True)
#         df_temp_MAX.rename(columns={'avgTemp':name}, inplace=True)
#         df_temp_combined=df_temp_MAX[['date', name]]
#         df_temp_combined['date']=pd.datetime(df_temp_combined['date'], errors='coerce')
#         bigdf['date']=df_temp_combined['date']
#         bigdf[names]=df_temp_combined[names]
#         bigdf[name]=df_temp_combined[name]
#%%
df_temp_MAX


# In[37]:


# Create empty lists to append the data into
dates_temp = []
temps = []
dates_prcp = []
prcp = []
temps_MAX=[]
temps_MIN=[]
dates_temp_MAX=[]
dates_temp_MIN=[]
# zip_codes=[97218,99336]
zip_codes=[97218]

names=['avgTemp_WA']
# names=['avgTemp_WW']
 # #initialize dataframe
df_temp_MAX = pd.DataFrame()
df_temp_MIN = pd.DataFrame()
df_temp_AVG = pd.DataFrame()
df_temp_combined=pd.DataFrame()
bigdf=pd.DataFrame()

for i,name in zip(range(len(zip_codes)), names):
    zip_=zip_codes[i]
    #Identify what years we want Temp and Prcp data for
    for year in range(2010, 2011):
        year = str(year)
        #Print out 'working on year' to idenfity if script is running correctly
        print('working on year '+year)
        #make the api call for temp and precipitation
        r = requests.get(f'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:{zip_}&datatypeid=TMAX&datatypeid=TMIN&units=standard&limit=1000&startdate='+year+'-01-01&enddate='+year+'-12-31', headers={'token':Token})
        
        #Load JSON data
        d = json.loads(r.text)
        print(d)
        # df = pd.DataFrame.from_dict(d, orient='columns')
        #e = json.loads(p.text)
        avg_temps_MAX = [item for item in d['results'] if item['datatype']=='TMAX']
        
        #get the date field from all average temperature readings
        dates_temp_MAX += [item['date'] for item in avg_temps_MAX]
        
        #get the actual average temperature from all average temperature readings
        temps_MAX += [item['value'] for item in avg_temps_MAX]
        
        # #populate date and average temperature fields (cast string date to datetime
        df_temp_MAX['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp_MAX]
        
        # Create a column for max temps
        df_temp_MAX['avgTemp'] = temps_MAX
        
        #convert daily summaries to monthly data
        df_temp_MAX = df_temp_MAX.set_index('date').resample('M').mean()




