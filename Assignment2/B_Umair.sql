SELECT name 
FROM restaurant 
WHERE cuisine = 'Indian';

SELECT distinct a.name 
FROM restaurant a 
INNER JOIN rating b 
ON a.rid = b.rid 
WHERE b.stars IN (4,5) 
ORDER BY a.name;

SELECT distinct a.name
FROM restaurant a 
LEFT OUTER JOIN rating b
ON a.rid = b.rid
WHERE b.rid IS NULL;

SELECT distinct a.name
FROM reviewer a 
FULL OUTER JOIN rating b
ON a.vid = b.vid
WHERE b.ratingdate IS NULL;

SELECT reviewer.name, restaurant.name
FROM reviewer, restaurant, 
    (SELECT r1.rid, r1.vid 
        FROM rating r1, rating r2 
        WHERE r1.rid=r2.rid 
        AND r1.vid=r2.vid 
        AND r2.ratingdate>r1.ratingdate 
        AND r2.stars>r1.stars
    ) M
WHERE reviewer.vid=M.vid 
AND restaurant.rid=M.rid;

SELECT restaurant.name, MAX(rating.stars)
FROM rating 
INNER JOIN restaurant
ON restaurant.rid=rating.rid
GROUP BY restaurant.name
ORDER BY restaurant.name;

SELECT restaurant.name, (MAX(stars) - MIN(stars)) spread
FROM restaurant
INNER JOIN rating
ON restaurant.rid=rating.rid
GROUP BY restaurant.name
ORDER BY spread DESC, restaurant.name;
    
SELECT AVG(INDO.avgstars) - AVG(CHIN.avgstars) AS Diff_Btw_Indo_Chin_Rating
FROM
    (SELECT r.name, r.cuisine, AVG(ra.stars) AS avgstars
        FROM restaurant r
        JOIN rating ra
        ON r.rid=ra.rid
        GROUP BY r.name, r.cuisine
        HAVING r.cuisine='Indian'
    ) INDO,
    (SELECT r.name, r.cuisine, AVG(ra.stars) AS avgstars
        FROM restaurant r
        JOIN rating ra
        ON r.rid=ra.rid
        GROUP BY r.name, r.cuisine
        HAVING r.cuisine='Chinese'
    ) CHIN