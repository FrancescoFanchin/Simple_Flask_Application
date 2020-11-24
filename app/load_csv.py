from pathlib import Path
import sqlite3
import pandas as pd

#connect to db
dbfile="input_database.db"
Path(dbfile).touch()
conn = sqlite3.connect(dbfile)
c = conn.cursor()
#create table
c.execute('''DROP TABLE IF EXISTS measures_table''')
c.execute(''' CREATE TABLE measures_table (id int, timestamp text,temperature text, duration text, uploaded_by text, request_timestamp text)''')
csv="input_data.csv"
df= pd.read_csv(csv)
df["uploaded_by"]="csv file"
df["request_timestamp"]=" "
df=df.sort_values(by=["id"])
print(df.head())
#feed the database
df.to_sql('measures_table',conn,if_exists='replace',index=False)



