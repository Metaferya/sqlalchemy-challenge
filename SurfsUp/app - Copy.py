from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
import numpy as np

app = Flask(__name__)

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the last data point
    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    a_year_before = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    
    # Query precipitation data for the last year
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= a_year_before).all()
    
    # Convert query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    results = session.query(Station.station).all()
    
    # Convert list of tuples into normal list
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

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

def convert_date(date_str):
    """Convert date from MMDDYYYY to YYYY-MM-DD format."""
    return dt.datetime.strptime(date_str, "%m%d%Y").strftime("%Y-%m-%d")

@app.route("/api/v1.0/start")
@app.route("/api/v1.0/start/end")
def stats(start=None, end=None):
    # Convert dates to YYYY-MM-DD format
    start_date = convert_date(start)
    end_date = convert_date(end) if end else None

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if end_date:
        # Calculate TMIN, TAVG, TMAX for dates between the start and end date inclusive
        results = session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    else:
        # Calculate TMIN, TAVG, TMAX for all dates greater than or equal to the start date
        results = session.query(*sel).filter(Measurement.date >= start_date).all()

    # Convert list of tuples into normal list
    temp_stats = list(np.ravel(results))
    return jsonify(temp_stats)

if __name__ == "__main__":
    app.run(debug=True)
