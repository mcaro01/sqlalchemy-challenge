# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

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
def home():
    return (
    f"<h1/>The available routes are:</h1></br>"
    f"<h2/></api/v1.0/precipitation <br/>"
    f"/api/v1.0/stations <br/>"
    f"/api/v1.0/tobs <br/>"
    f"/api/v1.0/start <br/>"
    f"/api/v1.0/start/end <br/></h2>"
    f"You must replace 'start' and 'end' with dates, such as 2016-08-23 (Year, month, day)!"
    )

@app.route("/api/v1.0/precipitation")
def Precipitation():
    session = Session(engine)

    #query1 = To retrieve the last 12 months of Precipitation
    recent_data_point = session.query(func.date(measurement.date)).order_by(func.date(measurement.date).desc()).all()
    year_ago = dt.date(2017,8,23)- dt.timedelta(days=365)
    precp_results = session.query(measurement.date, measurement.prcp).filter(func.date(measurement.date) >= year_ago).all()
    session.close()

    #create dictionary 
    Precp_Analysis = []
    count = 0
    for date, prcp in precp_results:
        dtprcp_dict = {}
        dtprcp_dict["date"] = precp_results[count][0]
        dtprcp_dict["prcp"] = precp_results[count][1]
        Precp_Analysis.append(dtprcp_dict)
        count = count + 1
       
    return jsonify(Precp_Analysis)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    #query2 = To List of stations 
    most_active_station_id = session.query(measurement.station).\
                               group_by(measurement.station).all()
    session.close()
    result = list(np.ravel(most_active_station_id))

    return jsonify(result)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    #query3 = Query the dates and temperature observations of the most-active station for the previous year of data.
    year_ago = dt.date(2017,8,23)- dt.timedelta(days=365)
    year_temp = session.query(measurement.date, measurement.tobs, measurement.station).\
      filter(measurement.date >= year_ago, measurement.station == 'USC00519281').all()
    session.close()
    result = list(np.ravel(year_temp))

    return jsonify(result)



@app.route("/api/v1.0/<start>")
def precip(start):
    session = Session(engine)

    #query4 =  list of the min temp,avg temp,max temp for a specified start.
    
    precp_results1 = session.query(measurement.date, func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).\
        filter(func.date(measurement.date) >= func.date(start)).group_by(func.date(measurement.date)).all()
    session.close()

    results = list(np.ravel(precp_results1))

    return jsonify(results)
    

@app.route("/api/v1.0/<start>/<end>")
def Precip(start, end):
    session = Session(engine)

    #query4 =  list of the min temp,avg temp,max temp for a specified start.
    
    precp_results1 = session.query(measurement.date, func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).\
        filter(func.date(measurement.date) >= func.date(start)).filter(func.date(measurement.date) <= func.date(end)).\
            group_by(func.date(measurement.date)).all()
    session.close()

    results = list(np.ravel(precp_results1))

    return jsonify(results)
   

if __name__ == "__main__":
    app.run(debug=True)