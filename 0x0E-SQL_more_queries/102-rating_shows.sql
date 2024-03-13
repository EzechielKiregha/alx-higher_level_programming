-- this lists all shows from hbtn_0d_tvshows_rate by their rating.
-- with recoreds ordered by descending rating.

SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS s_rating
       INNER JOIN `tv_show_ratings` AS s_rating_join
       ON s_rating.`id` = s_rating_join.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
