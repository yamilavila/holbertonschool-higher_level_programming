-- Task 9.Cities by States
-- Description: Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id 
-- You can use only one SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id;
