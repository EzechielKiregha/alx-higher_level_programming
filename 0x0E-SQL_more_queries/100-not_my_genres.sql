-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.

SELECT DISTINCT `name`
  FROM `tv_genres` AS n_genre
       INNER JOIN `tv_show_genres` AS s
       ON n_genre.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t_show
       ON s.`show_id` = t_show.`id`
       WHERE n_genre.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS n_genre
	             INNER JOIN `tv_show_genres` AS s
		     ON n_genre.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t_show
		     ON s.`show_id` = t_show.`id`
		     WHERE t_show.`title` = "Dexter")
 ORDER BY n_genre.`name`;
