# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

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
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
##################################################
# precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
# query the precipitation data for last 12 months
    prcp_query = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date >= '2016-08-23').\
                    order_by(Measurement.date).all()
    
#create an empty list of precipitation data
    prcp_data_list = []
#Create a dictionary from the row data and append to a list
    for date,  prcp in prcp_query:

        precipitation_dict = {}
        precipitation_dict["date"]= date
        precipitation_dict["prcipitaion"]= prcp
        prcp_data_list.append(precipitation_dict)

    return jsonify(prcp_data_list)
        
###################################################
# Station route

@app.route("/api/v1.0/stations")
def stations():
# query the names of the statons

    station_query = session.query(Station.station).all()

 # Convert list of tuples into normal list
    stations = list(np.ravel(station_query))

    return jsonify(stations)

###################################################
# Tobs route

@app.route("/api/v1.0/tobs")
def tobs():
# Most active station is USC00519281
# Most recent date on dataset is 2017-08-23

    tobs_query = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= '2016-08-23').\
            filter(Measurement.station == 'USC00519281').\
                order_by(Measurement.date).all()
    
 # Convert list of tuples into normal list    
    temperature_list = list(np.ravel(tobs_query))

    return jsonify(temperature_list)

#####################################################

@app.route("/api/v1.0/<start>")
def start_date(start):

    start_date_query = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()                                                                                                                                                                     

    temps_from_start = []
    for min, avg, max in start_date_query:
        tobs_dict= {}
       
        tobs_dict["TMIN"] = min
        tobs_dict["TAVG"] = avg
        tobs_dict["TMAX"] = max
        temps_from_start.append(tobs_dict)

        return jsonify(temps_from_start)
    
########################################################
    
@app.route("/api/v1.0/<start>/<end>") 
def start_end_date (start, end):

    
    start_end_date_query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    
    temps_in_btwn = []
    for min, avg, max in start_end_date_query:
        temps_in_dict= {}
       
        temps_in_dict["TMIN"] = min
        temps_in_dict["TAVG"] = avg
        temps_in_dict["TMAX"] = max
        temps_in_btwn.append(temps_in_dict)

        return jsonify(temps_in_btwn)
##########################################################   
session.close()

if __name__ == '__main__':
    app.run(debug=True)



