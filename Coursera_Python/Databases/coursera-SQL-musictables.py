import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# To create tables and its datas
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
        );

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
#for find the particular key from the file
#every song has a particular key
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')

for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue#find trackid's. means new song
    #find the datas about the song
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue
    #if there's no name, artist, album of a song that we're looking for.

    #add artist names to artist table
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]#this is foreign key
    #add album titles and foreign key's to album table
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]#foreign key

    if (name):
        #add genre names to genre table
        cur.execute('''INSERT OR IGNORE INTO Genre (name) 
                    VALUES ( ? )''', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
        try:
            genre_id = cur.fetchone()[0]#get foreign keys if not they are nonetype
        except TypeError:
            genre_id = 0
        #add all the stuffs to track table
        cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
                    (name, album_id, genre_id,
                     length, rating, count))

    conn.commit()
conn.close()
