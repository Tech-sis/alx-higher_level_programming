-- Script to count shows by genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(*) DESC;
