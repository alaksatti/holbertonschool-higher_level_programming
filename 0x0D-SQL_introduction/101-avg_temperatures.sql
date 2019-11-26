-- Import in hbtn_0c_0 database table dump.
-- display average temp by Fahrenheit by city ordered by decending temp
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC
