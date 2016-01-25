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
FirstName = str("FirstName")
form = cgi.FieldStorage()
if "FirstName" not in form:
    print("FirstName not in form")
else:
    Highscore = str(form.getvalue("FirstName"))
    print("Welcome " + FirstName + ".")


c.execute("INSERT INTO players VALUES (null, '%s', null)" % FirstName)

conn.commit()



