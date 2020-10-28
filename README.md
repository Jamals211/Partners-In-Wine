# <b> Partners In Wine <b>

<p align="center">
  <img src="Vineyard-chalk-soil.jpg" width="850">
</p>

Final Project

## Purpose
The purpose of this project is to determine how weather impacts the scores of wine.


## First Segment
My role in this project was to research data on weather and and global wine scores, import the data using APIs, merge the data, and clean the data.  NOAA and the Global Wine Score websites are terrific resources for finding weather and wine data. 

### Importing NOAA Data
NOAA has excellent documentation on their API that allowed us to pull maximum and minimum temperatures as well as precipitation. One challenge of this API is that there are different stations that have different data. One station might have maximum and minimum temperatures but not precipitation. Another station might have precipitation but only 80% of temperature data. I broke the code up into different stations for each For Loop in order to find the best stations with the least amount of NAN values. I also broke the code up into temperature and precipitation to identify stations within the same zip codes that had good data for the regions we were interested in.

### Importing Wine Data
The Global Wine Score website allowed us to search by country and color. We chose to focus on the US due to reliable and abundant weather data. 

### Merging The Data
Once the weather and wine data was imported using the APIs, we identified the weather data that had large errors and went back and checked more weather stations. Once we were satisfied with the data we had, we merged weather and wine data. We combined the weather and wine data using the appellations (areas where the wine was grown). Finally we cleaned the data by dropping NAN values and columns that were not needed.
