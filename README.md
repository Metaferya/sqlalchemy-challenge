# Climate Analysis and Flask API
## Overview
This repository contains two main components:

A Jupyter Notebook for climate data analysis using SQLAlchemy, Pandas, and Matplotlib.

A Flask API to serve climate data based on the analysis performed in the Jupyter Notebook.

## Requirements
Ensure you have the following installed:

Python 3.7 or later

Flask

SQLAlchemy

Pandas

Matplotlib

Jupyter Notebook

# Part 1: Climate Analysis using Jupyter Notebook

## File: Climate_Analysis.ipynb

This Jupyter Notebook performs exploratory analysis on the climate data stored in the hawaii.sqlite SQLite database. It includes the following steps:

**1.Reflecting Tables into SQLAlchemy ORM:**

Reflects the existing database tables measurement and station into SQLAlchemy classes.

**2.Exploratory Precipitation Analysis:**

Retrieves and plots the last 12 months of precipitation data.

**3.Exploratory Station Analysis:**

Calculates the total number of stations.

Identifies the most active stations and their temperature statistics.

**4.Plotting Results:**

Visualizes precipitation and temperature data using Matplotlib.

**How to Run**

1.Open a terminal and navigate to the repository directory.

2.Launch Jupyter Notebook.

3.Open Climate_Analysis.ipynb and run the cells sequentially.

# Part 2: Flask API

## File: app.py

This Flask application serves climate data via a RESTful API. The endpoints include:

* /: Lists all available routes.

* /api/v1.0/precipitation: Returns precipitation data for the last 12 months.

* /api/v1.0/stations: Returns a list of all stations.

* /api/v1.0/tobs: Returns temperature observations for the most active station over the last 12 months.

* /api/v1.0/<start>: Returns minimum, average, and maximum temperatures for dates greater than or equal to the start date in MMDDYYYY format.

* /api/v1.0/<start>/<end>: Returns minimum, average, and maximum temperatures for the date range specified in MMDDYYYY format.

**How to Run**

1.Open a terminal and navigate to the repository directory.

2.Run the Flask application.

3.Open a web browser and navigate to the following URLs to test the endpoints:

+ Home: http://127.0.0.1:5000/

+ Precipitation: http://127.0.0.1:5000/api/v1.0/precipitation

+ Stations: http://127.0.0.1:5000/api/v1.0/stations

+ Temperature Observations: http://127.0.0.1:5000/api/v1.0/tobs

+ Stats (Start Date): http://127.0.0.1:5000/api/v1.0/01012017

+ Stats (Start and End Date): http://127.0.0.1:5000/api/v1.0/01012017/12312017

