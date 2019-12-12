
--PART-1 (A)*************************************************************************************
DROP TABLE Restaurant_Locations;
CREATE TABLE Restaurant_Locations(
        rID int,
        name varchar2(100),
        street_address varchar2(100),
        city varchar2(100),
        state varchar2(10),
        zipcode number(5),
        cuisine varchar2(100));

--PART-1 (B)*************************************************************************************
DECLARE
  A Restaurant_Locations.rID%TYPE;
  B Restaurant_Locations.name%TYPE;
  C Restaurant_Locations.name%TYPE;
  D Restaurant_Locations.street_address%TYPE;
  E Restaurant_Locations.city%TYPE;
  F Restaurant_Locations.state%TYPE;
  G Restaurant_Locations.zipcode%TYPE;
  H Restaurant_Locations.cuisine%TYPE;

  CURSOR RLCursor IS
         SELECT rID, name, address, cuisine
         FROM Restaurant;    

BEGIN

  OPEN RLCursor;
  
  LOOP
     FETCH RLCursor INTO A,B,C,H;
     SELECT REGEXP_SUBSTR(C, '^\d+\s+[A-Z]{1}\s+[A-Z][a-z]+\s+[A-Z][a-z]+') INTO D FROM dual;
     SELECT REGEXP_SUBSTR(C, 'C[a-z]+go') INTO E FROM dual;
     SELECT REGEXP_SUBSTR(C, '[A-Z]{2}') INTO F FROM dual;
     SELECT REGEXP_SUBSTR(C, '\d{5}$') INTO G FROM dual;
     EXIT WHEN RLCursor%NOTFOUND;
     INSERT INTO Restaurant_Locations VALUES(A,B,D,E,F,G,H);
  END LOOP;
  
  CLOSE RLCursor;

END;
/

SELECT * FROM Restaurant_Locations;