#********************************Retrieving Data by Using Pandas Library************************************************


#csv = comma separated values
#tsv = tab separated values
#ssv = space separated values
#query = sorgu
#expand = genişletmek, büyütmek
#cursor = imleç, gösterge
#parse = ayrıştırmak
import pandas as pd
import _sqlite3 as sq3

from Tools.scripts.dutree import display
from pymongo import MongoClient#this is common noSQL database


#Reading csv, tsv, ssv files
#filepath = /blabla.csv
#data = pd.read_csv(filepath) to read a csv file
#data = pd.read_csv(filepath, sep='\t') to read a tsv file
#data = pd.read_csv(filepath, delim_whitespace=True) to read a ssv file
#data = pd.read_csv(filepath, header=None)Don't use first row for column name(it has column names)
#data = pd.read_csv(filepath, names=['Name1', 'Name2']) to specify column names




#Read JSON file as dataframe
#data = pd.read_json(filepath)
#data.to_json('outputfile.json') to write it



#Reading SQL Data
#path = 'classic_rock.db'
#con = sq3.Connection(path) Create connection to db
#query = '''SELECT * FROM rock_songs; write query
#'''
#data = pd.read_sql(query, con) Execute query




# Most NOSQL databases store data as JSON format**********************
#con = MongoClient() create mongo connection
#db = con.database_name choose database, con.list_database_names() will display available databases
#cursor = db.connection_name.find(query) create a cursor object using query, to specify it. find it and it will be our query
#df = pd.DataFrame(list(cursor)) expand cursor and construct DataFrame




#API and Data Cloud Access
#data_url = 'blabla.data' it's a URL such as twitter...
#df = pd.read_csv(data_url, header=None) read data into pandas




#Example
path = 'classic_rock.db'
con = sq3.Connection(path)
query = '''SELECT * FROM rock_songs;
'''
#select by artist and release year, count the number of the songs as num_songs
#find the average play count of those songs using AVG function and call that avg_plays
#pull them from rock_songs, group them by artist and release year and order them by num_songs from largest to smallest
query1 = '''SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays
    FROM rock_songs
    GROUP BY Artist, Release_Year
    ORDER BY num_songs desc;
'''

observations = pd.read_sql(query1, con)
#coerce_float = doesn't effect this dataset, because floats were correctly parsed
#parse_dates = parse release year as a date
#chunksize = allows for streaming results as a series of shorter tables
observations_generator = pd.read_sql(query1, con, coerce_float=True, parse_dates=['Release_Year']
                                     , chunksize=5)
#to execute observations_generator as shorter tables
for index, observations in enumerate(observations_generator):
    if index < 5:
        print(f'Observation index: {index}'.format(index))
        print(observations)

#print(observations)#the beatles have released 23 song in 1967. and they had an average numb of 6.5




