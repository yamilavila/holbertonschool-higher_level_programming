-- Task 8.Cities of Cali
-- script that lists all the cities of California that can be found in the database
-- Description: states table contains only one record where name = California (but the id can be different),
-- Results must be sorted in ascending order by cities.id,
-- Not allowe to use JOIN
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
)
ORDER BY cities.id;
