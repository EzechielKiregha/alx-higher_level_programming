-- this lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- where records are ordered by descending rating.

SELECT `name`, SUM(`rate`) AS `rating`

  FROM `tv_genres` AS s_rating
       INNER JOIN `tv_show_genres` AS s_rating_join
       ON s_rating_join.`genre_id` = s_rating.`id`
       INNER JOIN `tv_show_ratings` AS res_rating
       ON res_rating.`show_id` = s_rating_join.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
