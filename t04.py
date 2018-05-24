# Installation of mysql-connector

# brew install protobuf
# export MYSQLXPB_PROTOBUF_INCLUDE_DIR=/usr/local/opt/protobuf/include
# export MYSQLXPB_PROTOBUF_LIB_DIR=/usr/local/opt/protobuf/lib
# export MYSQLXPB_PROTOC=/usr/local/opt/protobuf/bin/protoc
# pip install mysql-connector==2.1.4

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'northwind'
}

connection = cur = None
try:
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute('select * from categories')
    for row in cur.fetchall():
        print(row[0], row[1], row[2], sep=", ")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if cur:
        cur.close()
    if connection:
        connection.close()