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
Highscores = str("HighScores")
form = cgi.FieldStorage()
if "HighScores" not in form:
    print("HighScores not in form")
else:
    Highscore = str(form.getvalue("HighScores"))
    print("The top 10 Highscores are: ")


c.execute("SELECT 10 from scores")

print([(r0]) for r in c.fetchall()])




