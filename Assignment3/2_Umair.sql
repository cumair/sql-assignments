
--PART-2 (A)*********************************************************************
set serveroutput on;
CREATE OR REPLACE PROCEDURE restaurant_insert
   (i_RestaurantName    IN restaurant.name%TYPE,
   i_UserName           IN reviewer.name%TYPE,
   i_Rating             IN rating.stars%TYPE,
   i_RatingDate         IN rating.ratingdate%TYPE) AS

        i_RatingRID          rating.rid%TYPE;
        i_RatingVID          rating.vid%TYPE;
        i_temp               reviewer.name%TYPE;
        
BEGIN
       SELECT MAX(vid) + 1 INTO i_temp FROM reviewer;
       
       INSERT INTO reviewer (vid, name) SELECT i_temp,i_UserName 
       FROM dual 
       WHERE i_UserName 
       NOT IN (SELECT name FROM reviewer);

       SELECT rid INTO i_RatingRID FROM restaurant WHERE i_RestaurantName = restaurant.name;
       SELECT vid INTO i_RatingVID FROM reviewer WHERE i_UserName = reviewer.name;
       
       INSERT INTO rating (rid, vid, stars, ratingdate)
       VALUES(i_RatingRID, i_RatingVID, i_Rating, i_RatingDate);   
       DBMS_OUTPUT.PUT_LINE(i_RatingRID || i_RatingVID || i_Rating || i_RatingDate);
END;
/
--PART-2 (B)*****************************************************************************************
DROP TABLE Top5Restaurants;
CREATE TABLE Top5Restaurants(rID int, stars int, name varchar2(100));

CREATE or REPLACE TRIGGER Top5
AFTER INSERT
ON rating

DECLARE
    temp_rid rating.rid%TYPE;
    temp_stars rating.stars%TYPE;
    temp_name restaurant.name%TYPE;

    CURSOR Top5Cursor IS
        SELECT sub1.rid, avg_stars, name FROM 
            (SELECT rid, AVG(stars) avg_stars FROM rating GROUP BY rid) sub1,
            (SELECT rid, name FROM restaurant) sub2
        WHERE sub1.rid = sub2.rid
        ORDER BY avg_stars DESC
        FETCH FIRST 5 ROWS ONLY;

BEGIN
    DELETE FROM Top5Restaurants; 
    
    OPEN Top5Cursor;
    
    LOOP
        FETCH Top5Cursor INTO temp_rid, temp_stars, temp_name;
        EXIT WHEN Top5Cursor%NOTFOUND;
        INSERT INTO Top5Restaurants (rid, stars, name) 
        VALUES (temp_rid, temp_stars, temp_name);
    END LOOP;
    
    CLOSE Top5Cursor;
            
END; 
/ 
--PART-2 (C)****************************************************************************************
BEGIN
  restaurant_insert('Jade Court','Sarah M.', 4, DATE '2017-08-17');  
  restaurant_insert('Shanghai Terrace','Cameron J.', 5, DATE '2017-08-17');
  restaurant_insert('Rangoli','Vivek T.', 3, DATE '2017-09-17');
  restaurant_insert('Shanghai Inn','Audrey M.', 2, DATE '2017-07-08');
  restaurant_insert('Cumin','Cameron J.', 2, DATE '2017-09-17');

END;
/
SELECT * FROM rating;
SELECT * FROM reviewer;
SELECT * FROM Top5Restaurants;
--**************************************************************************************************

/*IGNORE BELOW STATEMENTS

DELETE FROM reviewer WHERE name = 'Audrey M.';
DELETE FROM rating WHERE ratingdate = DATE '2017-08-17';
DELETE FROM rating WHERE ratingdate = DATE '2017-09-17';
DELETE FROM rating WHERE ratingdate = DATE '2017-07-08';
DELETE FROM Top5Restaurants;*/










