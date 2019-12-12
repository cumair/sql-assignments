# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:48:35 2019

@author: mkalo
"""

'''********************************
         UMAIR CHAANDA
DSC 450   ASSIGNMENT-4    PART-4
***********************************'''
import json
import sqlalchemy, os

from sqlalchemy import create_engine

filename="library2.db"

if os.path.exists(filename):
    os.remove(filename)

engine = create_engine('sqlite:///library2.db', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

metadata = MetaData()

Tweet_Table = Table('Tweets', metadata,
                      Column('created_at', String),
                      Column('id_str',Integer, primary_key=True),
                      Column('text',String),
                      Column('source',String),
                      Column('in_reply_to_user_id',String),
                      Column('in_reply_to_screen_name',String),
                      Column('in_reply_to_status_id',String),
                      Column('retweet_count',Integer),
                      Column('contributors',String))

metadata.create_all(engine)

insert_stmt = Tweet_Table.insert(bind=engine)

type(insert_stmt)

print (insert_stmt)

compiled_stmt = insert_stmt.compile()
print(compiled_stmt.params)

datafile = open('Tweet1_Assignment4.txt','r', encoding='utf8')
List_Tweet = datafile.readline().split('EndOfTweet')
datafile.close()

for line in List_Tweet:
    jsonDecode = json.loads(line)
    col1 = jsonDecode.get('created_at')
    col2 = jsonDecode.get('id_str')
    col3 = jsonDecode.get('text')
    col4 = jsonDecode.get('source')
    col5 = jsonDecode.get('in_reply_to_user_id')
    col6 = jsonDecode.get('in_reply_to_screen_name')
    col7 = jsonDecode.get('in_reply_to_status_id')
    col8 = jsonDecode.get('retweet_count')
    col9 = jsonDecode.get('contributors')
    
    insert_stmt.execute(created_at=col1, 
                        id_str=col2,
                        text=col3,
                        source=col4,
                        in_reply_to_user_id=col5,
                        in_reply_to_screen_name=col6,
                        in_reply_to_status_id=col7,
                        retweet_count=col8,
                        contributors=col9,
                        )

metadata.bind = engine

select_stmt = Tweet_Table.select(Tweet_Table.c.source.like('%iphone%' or '%android%'))
result = select_stmt.execute()

select_stmt_2 = Tweet_Table.select(Tweet_Table.c.in_reply_to_user_id==None)
result_2 = select_stmt_2.execute()

counter = 0
counter_2 = 0

for r in result:
    counter += 1

for r in result_2:
    counter_2 += 1

print('There are total ' +str(counter)+ ' iphone and android users.')
print('There are total ' +str(counter_2)+ ' tweets with users who are not replying.')
    
sql = text('DROP TABLE IF EXISTS Tweets;')
result = engine.execute(sql)