import pymysql.cursors
from secret import *
from google.cloud.sql.connector import Connector
import sqlalchemy

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        SQL_INSTANCE,
        "pymysql",
        user=SQL_NAME,
        password=SQL_PASS,
        db="Guess the Lyric"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)




connector.close()