# Import the dependencies.
import datetime as dt
import numpy as np

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
def Welcome():
    return(
        f"Welcome to the  Hawii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.<p>"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data from last year"""
    # Calculate the date one year from the last date in data set.
    a_year_before = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= a_year_before).all()
    
    session.close()

    #Dict with date as a key and prcp as a value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

session.close()

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    results = session.query(Station.station).all()
    
    # Convert list of tuples into normal list
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

session.close()

@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date one year ago from the last data point
    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    a_year_before = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Query temperature observations for the most active station for the last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= a_year_before).all()
    
    # Convert list of tuples into normal list
    tobs_list = [temp[0] for temp in results]
    return jsonify(tobs_list)

session.close()

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # Calculate TMIN, TAVG, TMAX for all dates greater than or equal to the start date
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        # Calculate TMIN, TAVG, TMAX for dates between the start and end date inclusive
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Convert list of tuples into normal list
    temp_stats = list(np.ravel(results))
    return jsonify(temp_stats)

session.close()

if __name__ == "__main__":
    app.run(debug=True)
