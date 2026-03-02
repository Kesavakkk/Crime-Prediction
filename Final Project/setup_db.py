import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

mydb = pymysql.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', 'root')
)

cursor = mydb.cursor()

with open(r'static/database.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    
for statement in sql_script.split(';'):
    statement = statement.strip()
    if statement:
        cursor.execute(statement)

mydb.commit()
cursor.close()
mydb.close()
print('Database created successfully!')
