# sqlalchemy-challenge

Part 1: Analyze and Explore the Climate Data
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. Specifically,used SQLAlchemy ORM queries, Pandas, and Matplotlib

Used SQLAlchemy create_engine to connect to your sqlite database.

Used SQLAlchemy automap_base() to reflect your tables into classes and saved the references to those classes called Station and Measurement.


## Precipitation Analysis

Design a query to retrieve the last 12 months of precipitation data.

Select only the date and prcp values.

Load the query results into a Pandas DataFrame and set the index to the date column.

Sort the DataFrame values by date.

Plot the results using the DataFrame plot method.

Use Pandas to print the summary statistics for the precipitation data.

## Station Analysis

Design a query to calculate the total number of stations.

Design a query to find the most active stations.

List the stations and observation counts in descending order.

Which station has the highest number of observations?

Hint: You may need to use functions such as func.min, func.max, func.avg, and func.count in your queries.

Design a query to retrieve the last 12 months of temperature observation data (TOBS).

Filter by the station with the highest number of observations.

Plot the results as a histogram with bins=12.
