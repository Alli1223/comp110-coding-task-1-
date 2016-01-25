#!/usr/bin/python

#Turn on debug mode.
import cgitb
cgitb.enable()

#Print necessary headers.
print("Content-Type: text/html")
print()

#Connect to the database.
import pymysql
conn = pymysql.connect(
    db = 'example',
    user='root',
    passwd='databasepassword',
    host='localhost')
c = conn.cursor()

import cgi
score = str("score")
form = cgi.FieldStorage()
if "score" not in form:
    print("score not in form")
else:
    score = str(form.getvalue("score"))


#insert the variables into scores
c.execute("INSERT INTO scores VALUES ('%s', '%s', '%s')", (player_id, level_id, score))

conn.commit()

#print the second column for all the data in scores
print([r[2]) for r in c.fetchall()])



