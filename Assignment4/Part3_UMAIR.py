# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:22:00 2019

@author: mkalo
"""

'''
***********************************
         UMAIR CHAANDA
DSC 450   ASSIGNMENT-4    PART-3
***********************************
'''

import sqlite3
import json

conn = sqlite3.connect('csc455.db')
c = conn.cursor()

Table_User = '''CREATE TABLE user
(
    id VARCHAR(35),
    name VARCHAR(70),
    screen_name VARCHAR(50),
    description VARCHAR(50),
    friends_count NUMBER(150),
    
    CONSTRAINT user_PK
    PRIMARY KEY(id)
);'''

Table_Tweets2 = '''CREATE TABLE Tweets2
(
    created_at VARCHAR(60),
    id_str NUMBER(60),
    text VARCHAR(180),
    source VARCHAR(90),
    in_reply_to_user_id VARCHAR(25),
    in_reply_to_screen_name VARCHAR(25),
    in_reply_to_status_id VARCHAR(25),
    retweet_count NUMBER(6),
    contributors VARCHAR(40),
    user_id VARCHAR(35),
    
    CONSTRAINT Tweets2_FK
    FOREIGN KEY(user_id) REFERENCES user(id)
);'''

c.execute("DROP TABLE IF EXISTS user")
c.execute(Table_User)
c.execute("DROP TABLE IF EXISTS Tweets2")
c.execute(Table_Tweets2)

errorfile = open('Assignment4_errors.txt','w')
datafile = open('Tweet2_Assignment4.txt','r', encoding='utf8')

dict_hfc = {}

#Spyder on my machine hanged and causing problems running large number of tweets
#that is why i am using range() to run small number of tweets
#change the number inside range() to run bigger number of tweets
for i in range(50000): 
    LineOne = datafile.readline()

    try:
        jsonDict = json.loads(LineOne)
        userValues = (jsonDict['user']['id'],
                      jsonDict['user']['name'],
                      jsonDict['user']['screen_name'],
                      jsonDict['user']['description'],
                      jsonDict['user']['friends_count']
                      )
        c.execute('INSERT OR IGNORE INTO user VALUES(?,?,?,?,?);',userValues)
        
        Tweets2Values = (jsonDict['created_at'],
                         jsonDict['id_str'],
                         jsonDict['text'],
                         jsonDict['source'],
                         jsonDict['in_reply_to_user_id'],
                         jsonDict['in_reply_to_screen_name'],
                         jsonDict['in_reply_to_status_id'],
                         jsonDict['retweet_count'],
                         jsonDict['contributors'],
                         jsonDict['user']['id']
                         )
        c.execute('INSERT INTO Tweets2 VALUES(?,?,?,?,?,?,?,?,?,?);',Tweets2Values)
        
        dict_hfc[jsonDict['user']['id'], jsonDict['user']['name']] = jsonDict['user']['friends_count']
                        
    except(ValueError):
        damaged_tweets = 'Tweet number ' + str(i) + ' IS DAMAGED TWEET \n'
        errorfile.write(damaged_tweets)

errorfile.close()
datafile.close()

'''
****************************************************************
             COMPUTATION FOR HIGHEST friend_count
****************************************************************
'''
query1 = c.execute(
        "SELECT id, name FROM user WHERE friends_count = (SELECT MAX(friends_count) FROM user);"
        ).fetchall()
print('User with highest friend_count: ' +str(query1))

'''
****************************************************************
PYTHON CODE TO PERFORM SAME COMPUTATION FOR HIGHEST friend_count
****************************************************************
'''
for key, value in dict_hfc.items():
    if value == max(dict_hfc.values()):
        print("User {}, with the highest friend_count at: {}".format(key, value))

'''
****************************************************************
            TWEETS WITHOUT ASSOCIATED USER ID ENTRY
****************************************************************
'''
query2 = c.execute(
        "SELECT * FROM user WHERE id IS NULL;"
        ).fetchall()
print('Tweets without associated user id entry: ' +str(query2))

   


conn.commit()
conn.close()








