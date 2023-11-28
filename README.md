# sqlalchemy-challenge

The project is to do climate analysis before planning a trip to Honolulu, Hawaii. Python, SQLAlchemy for the analysis, MatPlotLab for the visualizations and Flask for creating climate app.

Part 1: Analyze and explore the climate data.

•	Use SQLAlchemy create_engine to connect to sqlite database.
•	Reflect tables into classes and save a reference to those classes called Station and Measurement.

Precipitation Analysis

•	Design a query to retrieve the last 12 months of precipitation data.
•	Select only the date and prcp values.
•	Load the query results into a Pandas DataFrame and set the index to the date column.
•	Sort the DataFrame values by date.
•	Plot the results using the DataFrame plot method.

Station Analysis

•	Design a query to calculate the total number of stations.
•	Design a query to find the most active stations, and list the stations and observation counts in descending order.
•	Design a query to retrieve the last 12 months of temperature observation data (tobs).
•	Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

Part 2 - Climate App

•	Create routes
•	Convert the query results to a dictionary and return the JSON representation of it
•	Query the dates and temperature observations of the most active station for the last year of data.
•	Return a JSON list of temperature observations (TOBS) for the previous year.
•	Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
•	Calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
•	Calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
