-- this lists all shows contained in hbtn_0d_tvshows
-- that has genre as a null value

SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.show_id IS NULL
    ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
