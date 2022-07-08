-- Task 13.Number of shows by genre
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre
SELECT 
tv_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv__genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
