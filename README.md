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

3. Open Climate_Analysis.ipynb and run the cells sequentially.

