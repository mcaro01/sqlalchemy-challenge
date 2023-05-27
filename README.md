# sqlalchemy-challenge

![image](https://github.com/mcaro01/sqlalchemy-challenge/assets/125619215/19820297-b03b-4bb0-b31e-af8c35afe881)

  ## Part 1: Analyze and Explore the Climate Data

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.

Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

Use SQLAlchemy create_engine to connect to your sqlite database.

Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

## Precipitation Analysis

Design a query to retrieve the last 12 months of precipitation data.

Select only the date and prcp values.

Load the query results into a Pandas DataFrame and set the index to the date column.

Sort the DataFrame values by date.

Plot the results using the DataFrame plot method.

![image](https://github.com/mcaro01/sqlalchemy-challenge/assets/125619215/5ecd3ca4-aca2-4eef-a281-3c0e03d3c43c)


Use Pandas to print the summary statistics for the precipitation data.



## Station Analysis

Design a query to calculate the total number of stations.

Design a query to find the most active stations.

     List the stations and observation counts in descending order.

     Which station has the highest number of observations?

Design a query to retrieve the last 12 months of temperature observation data (TOBS).

    Filter by the station with the highest number of observations.

    Plot the results as a histogram with bins=12.
    
 ![image](https://github.com/mcaro01/sqlalchemy-challenge/assets/125619215/24c22daf-6cc5-4e71-97e9-713700131e73)

    
    
    
## Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. 
To do so, use Flask to create your routes as follows:

  ## 1)/

      Start at the homepage.

       List all the available routes.

## 2) /api/v1.0/precipitation

      Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as        the value.

      Return the JSON representation of your dictionary.

## 3) /api/v1.0/stations

      Return a JSON list of stations from the dataset.
     
## 4) /api/v1.0/tobs

      Query the dates and temperature observations of the most-active station for the previous year of data.

      Return a JSON list of temperature observations for the previous year.

## 5) /api/v1.0/<start> and /api/v1.0/<start>/<end>

      Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

      For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

      For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
  
 ## Hint
  
Join the station and measurement tables for some of the queries.

Use the Flask jsonify function to convert your API data to a valid JSON response object.


