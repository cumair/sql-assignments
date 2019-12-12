# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:52:03 2019

@author: mkalo
"""

'''********************************
         UMAIR CHAANDA
DSC 450   ASSIGNMENT-4    PART-1
***********************************'''

import sqlite3
import json

conn = sqlite3.connect('csc455.db')
c = conn.cursor()

Tweet1Table = '''CREATE TABLE Tweets
(
    created_at VARCHAR(60),
    id_str NUMBER(60),
    text VARCHAR(180),
    source VARCHAR(90),
    in_reply_to_user_id VARCHAR(25),
    in_reply_to_screen_name VARCHAR(25),
    in_reply_to_status_id VARCHAR(25),
    retweet_count NUMBER(6),
    contributors VARCHAR(40)
);'''

c.execute("DROP TABLE IF EXISTS Tweets")
c.execute(Tweet1Table)

datafile = open('Tweet1_Assignment4.txt','r', encoding='utf8')
List_Tweet = datafile.readline().split('EndOfTweet')
datafile.close()

for line in List_Tweet:
    jsonDecode = json.loads(line)
    allvalues = (jsonDecode.get('created_at'),
                 jsonDecode.get('id_str'),
                 jsonDecode.get('text'),
                 jsonDecode.get('source'),
                 jsonDecode.get('in_reply_to_user_id'),
                 jsonDecode.get('in_reply_to_screen_name'),
                 jsonDecode.get('in_reply_to_status_id'),
                 jsonDecode.get('retweet_count'),
                 jsonDecode.get('contributors'))
    c.execute('INSERT INTO Tweets VALUES (?,?,?,?,?,?,?,?,?);',allvalues)

query1 = c.execute(
        "SELECT COUNT(*) FROM Tweets WHERE source LIKE '%iphone%' OR '%android%';"
        ).fetchall()

query2 = c.execute(
        "SELECT COUNT(*) FROM Tweets WHERE in_reply_to_user_id IS NULL;"
        ).fetchall()

print(query1)
print(query2)




conn.commit()
conn.close()








