import pandas as pd
import _sqlite3 as sq3

path = 'baseball.db'

con = sq3.Connection(path)

query = '''SELECT * FROM allstarfull;
'''

print(pd.read_sql(query, con).head())

print(pd.read_sql('SELECT * FROM sqlite_master', con))#to see the all the different tables


#Select playerID's, find who played the most games and their avg of startingpos from allstarfull data
#group them by playerID and order them by number of the games played by player largest to smallest and startingpos avg smallest to largest
#show only first 3
query1 = '''SELECT playerID,
        sum(GP) AS num_of_games_played,
        AVG(startingPos) AS started_pos_av
        FROM allstarfull
        GROUP BY playerID
        ORDER BY num_of_games_played DESC, started_pos_av ASC
        LIMIT 3;
'''

print(pd.read_sql(query1, con))