# **Overview:**
    This challenge contains analysis on my holiday plans. I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I needed to take to accomplish this task. I was given the csv files containing the information on the climate and the station. By using both the csv file, I have used my logic to help me make the decision on my vacation. 

#### 1. Precipitation analysis: 
    First, I analyzed the precipitation data. To do so, I used the most recent data set. Here, I used the timedelta to find out the data of one year for the most recent date.Using that date, I got the previous 12 months of precipitation data.Then, I selected only the "date" and "prcp" values and loaded the values into a pandas dataframe, named the columns and shorted the dataframe by date. Finally, I ploted it using matplotlib to make easiar to read the data and make conclusions. 
 
#### 2. Station Analysis:
    Here, I started by desinging a query to calculate the total number of stations in the dataset. Then, I queried to find the most active stations, that is, the station that have the most rows. To do so, I listed the stations and observation. Then, I used the count function to count each station and arranged them in descending order to acknowledge the most active station.After that, I calculated the lowest, highest, and average temperatures that filters on the most-active station id found. At the end, I plotted all the temperature observations data and showed the result into the histogram to help me better understand the data.

#### 3. Design the climate app: 
    Here in this part, I have designed a Flask API based on the queries that I developed. To do so, I used Flask to create my routes. First, I created a route for precipitation that returns the jsonified precipitation data for the last year in the database. Next, I created route for station. This returns  jsonified data of all of the stations in the database. Third is tobs route. This route returns the jsonified data for the last year of data. Then, I created start route which returns the min, max, and average temperatures calculated from the given start date to the end of the dataset. Finally, the route for start and end date. It returns the min, max, and average temperatures calculated from the given start date to the given end date.
 
##### This project has file for resources of the analysis, and queries for the data analysis part, python file for the climate api and the readme file. They are saved as:

1. [README.md](https://github.com/shikhasitaula/sqlalchemy_challenge/blob/main/README.md): Provides orientation for this challenge.
2. [climate_starter.ipynb](https://github.com/shikhasitaula/sqlalchemy_challenge/blob/main/climate_starter.ipynb): It contains logic for the data manipulation. It is the jupyter notebook.
3. [app.py](https://github.com/shikhasitaula/sqlalchemy_challenge/blob/main/app.py): It carries the logic for the climate api. It is the python file.
4. [Resources](https://github.com/shikhasitaula/sqlalchemy_challenge/tree/main/Resources): It contains the csv files that we used for this chanllenge.