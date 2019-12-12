#importing sqlite3 DB
import sqlite3
#connect to DB
conn = sqlite3.connect('csc455.db')
#request a cursor from DB
c = conn.cursor()
#declare variable ZipcodeTable with create table statement
ZipcodeTable = '''CREATE TABLE ZipCode
(
  zip integer(5),
  city VARCHAR(100),
  state VARCHAR(10),
  latitude VARCHAR(25),
  longitude VARCHAR(25),
  timezone integer(1),
  dst integer(1)
  ); '''

#drop table ZipCode if already exists
c.execute("DROP TABLE IF EXISTS ZipCode")
#create table ZipCode
c.execute(ZipcodeTable)
#open and read file
datafile = open('ChIzipcode.csv','r')
#read all lines from ChIzipcode.csv into variable reading
reading = datafile.readlines()
#closing file ChIzipcode.csv
datafile.close()
#eliminate first row of file
datalines = reading[1:]
#add data into SQL table ZipCode
for line in datalines:
    stringSplit = line.strip().split(', ')
    stringSplit2 = line.split(',')
    for u,i in enumerate(stringSplit2):
        if i == 'NULL':
            stringSplit2[u] = None
    c.execute("INSERT INTO ZipCode VALUES(?,?,?,?,?,?,?);",stringSplit2)


#declare variable Res_Loc_Table with create table statement
ResLocTable = '''CREATE TABLE RESTAURANT_LOCATIONS
(
   rID INTEGER,
   name VARCHAR(100),
   street_address VARCHAR(100),
   city VARCHAR(100),
   state VARCHAR(10),
   zipcode INTEGER(5),
   cuisine VARCHAR(100));'''

#drop table RESTAURANT_LOCATIONS if already exists
c.execute("DROP TABLE IF EXISTS RESTAURANT_LOCATIONS")
#create table RESTAURANT_LOCATION
c.execute(ResLocTable)
#open and read file
datafile2 = open('export_restaurant_location.txt','r')
#read all lines from export_restaurant_location into variable reading2
reading2 = datafile2.readlines()
#closing file export_restaurant_location.txt
datafile2.close()
#declare reading2 to new variable datalines2
datalines2 = reading2
#insert data into SQL table RESTAURANT_LOCATIONS
for line in reading2:
    stringSplit3 = line.strip().split(', ')
    print (stringSplit3)


conn.commit()
conn.close()
