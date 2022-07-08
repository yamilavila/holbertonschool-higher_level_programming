-- Task 10.Genre ID by show
-- script that lists all shows contained in hbtn_0d_tvshows
-- Description: Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT 
tv_shows.title, 
tv_show_genres.genre.id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
