import psycopg2
import itertools


DB_HOST="127.0.0.1"
DB_DATABASE="minorproject"
DB_USERNAME="postgres"
DB_PASSWORD="12postgres34"



connection = psycopg2.connect(dbname = DB_DATABASE, user = DB_USERNAME, password = DB_PASSWORD, host = DB_HOST)

cursor = connection.cursor()

cursor.execute("SELECT url FROM jobs;")
stored_links = cursor.fetchall()
stored_links = list(itertools.chain(*stored_links))

# Python code to convert list of tuple into list

# Using itertools


connection.commit()
cursor.close()
connection.close()