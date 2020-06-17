#it's an example which we did with dictionaries before.

import sqlite3

conn = sqlite3.connect('email.sqlite')#creates new file for sqlite if not exists!
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')#if there is a table named Counts then use it

cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')#else, create a table named Counts

fh = open('mbox.txt', 'r')

for line in fh:
    if not line.startswith('From: '):
        continue

    pieces = line.split()
    email = pieces[1]#find emails from file
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()#create row
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))#if there is not row, then insert
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE email = ? ''', (email,))#else update them
    conn.commit()#store it into memory and write it to disk

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'#gonna order them by count numbers

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])#and print them
cur.close()



