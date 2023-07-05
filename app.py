# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()


# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
    
   f"Welcome to the Climate Analysis API!</br>"
   f"Available Routes:</br>"
   f"/api/v1.0/precipitation</br>"
   f"/api/v1.0/stations</br>"
   f"/api/v1.0/tobs</br>"
   f"/api/v1.0/<start></br>"
   f"/api/v1.0/<start>/<end></br>"
    )

@app.route("/api/v1.0/precipitation")
def Percipitation():
    recent_date = dt.date(2017 , 8, 23)
    one_year_date = recent_date - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date , Measurement.prcp).\
    filter(Measurement.date >= one_year_date).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")

def stations():
    station_names = session.query(Station.station).all()
    stations = list(np.ravel(station_names))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    one_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    temperature = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= one_year_date).all()
    temps = list(np.ravel(temperature))
    return jsonify(temps=temps)

@app.route("/api/v1.0/<start>")
def Start(start):
    date = start.split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    user_date = dt.date(year, month, day)
    min_max_avg = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= user_date).all()
    result = {}
    result['Minimum temperature'] = min_max_avg[0][0]
    result['Maximum temperature'] = min_max_avg[0][1]
    result['Average temperature'] = min_max_avg[0][2]
    return jsonify(result)
    

@app.route("/api/v1.0/<start>/<end>")
def Start_end(start, end):
    start_date = start.split("-")
    start_year = int(start_date[0])
    start_month = int(start_date[1])
    start_day = int(start_date[2])
    end_date = start.split("-")
    end_year = int(end_date[0])
    end_month = int(end_date[1])
    end_day = int(end_date[2])
    user_start_date = dt.date(start_year, start_month, start_day)
    user_end_date = dt.date(end_year, end_month, end_day)
    min_max_avg = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= user_start_date).\
    filter(Measurement.date <= user_end_date).all()  
    result = {}
    result['Minimum temperature'] = min_max_avg[0][0]
    result['Maximum temperature'] = min_max_avg[0][1]
    result['Average temperature'] = min_max_avg[0][2]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
