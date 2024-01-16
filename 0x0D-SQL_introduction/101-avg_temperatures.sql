-- script to list avg temp per city
-- DML query for listing the temp
SELECT city,
 AVG(value) AS avg_temp
 FROM temperatures
 GROUP BY city
 ORDER BY AVG(value) DESC;
