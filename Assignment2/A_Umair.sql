SELECT * 
FROM animal 
WHERE acategory = 'rare' 
ORDER BY timetofeed;

SELECT aname, acategory 
FROM animal 
WHERE aname LIKE ('%bear%');

SELECT * 
FROM animal 
WHERE acategory IS NULL;

SELECT * 
FROM animal 
WHERE timetofeed BETWEEN 1 AND 2.5;

SELECT aname, acategory 
FROM animal 
WHERE aname LIKE ('%tiger%') 
AND acategory != 'common';

SELECT aname 
FROM animal 
WHERE aname NOT LIKE ('%tiger%');

SELECT min(timetofeed) AS minimum, max(timetofeed) AS maximum 
FROM animal;

SELECT avg(timetofeed) AS avg_feed_time_rare 
FROM animal 
WHERE acategory = 'rare';

SELECT zname, MIN(earning) 
FROM 
    (SELECT zookeeper.zname, (zookeeper.hourlyrate*animal.timetofeed) AS earning
        FROM animal 
        INNER JOIN handles 
        JOIN zookeeper
        ON handles.zookeepid = zookeeper.zid
        ON animal.aid = handles.animalid
    )
GROUP BY zname;

SELECT zname, zookeepid
FROM zookeeper 
INNER JOIN handles
ON zookeeper.zid=handles.zookeepid
GROUP BY zname, zookeepid
HAVING count(zookeepid) >=4;