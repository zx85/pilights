# import the necessary packages
from flask import Flask
import json
import mysql.connector
import os

app = Flask(__name__)

# configuration used to connect to MariaDB
# Database credentials for the conkers
dbInfo = { "dbuser" : os.environ.get('dbUser'),
           "dbpass" : os.environ.get('dbPass'),
           "dbhost" : os.environ.get('dbHost'),
           "dbname" : os.environ.get('dbName'),
           "dbport" : os.environ.get('dbPort'),
           "dbtable" : os.environ.get('dbTable') }

from immersionSQL import routes
