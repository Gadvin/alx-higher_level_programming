-- script to show number of people with same score
-- DML query using GROUP BY for grouping purposes
SELECT score,COUNT(*) AS 'number' FROM second_table
 GROUP BY score
 ORDER BY score DESC;
