-- script that finds max temp for each state
-- DML query to list max temp by state
SELECT state,MAX(value) AS max_temp
 FROM temperatures
 GROUP BY state
 ORDER BY state;
