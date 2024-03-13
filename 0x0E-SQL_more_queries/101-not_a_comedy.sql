-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.

SELECT DISTINCT `title`
  FROM `tv_shows` AS t_show
       LEFT JOIN `tv_show_genres` AS s_genre
       ON s_genre.`show_id` = t_show.`id`
       LEFT JOIN `tv_genres` AS g
       ON g.`id` = s_genre.`genre_id`
       WHERE t_show.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS t_show
	             INNER JOIN `tv_show_genres` AS s_genre
		     ON s_genre.`show_id` = t_show.`id`

		     INNER JOIN `tv_genres` AS g
		     ON g.`id` = s_genre.`genre_id` WHERE g.`name` = "Comedy")
 ORDER BY `title`;
