import os
from dotenv import load_dotenv
load_dotenv()

APP_PORT=os.getenv('APP_PORT')
APP_ENV=os.getenv('APP_ENV')

SQL_DIALECT=os.getenv('SQL_DIALECT')

MYSQL_HOST=os.getenv('MYSQL_HOST')
MYSQL_DATABASE=os.getenv('MYSQL_DATABASE')
MYSQL_PORT=os.getenv('MYSQL_PORT')
MYSQL_USER=os.getenv('MYSQL_USER')
MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')