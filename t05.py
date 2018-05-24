### -------------- MySQL Client example Python --------------
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

new_categories = (
	(9, 'cat1', 'desc1'),
	(10, 'cat2', 'desc2'),
	(11, 'cat3', 'desc3')
	)

stmt = "insert into categories(category_id, category_name, description) values(%s, %s, %s)"

connection = cur = None
try:
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()

    cur.executemany(stmt, new_categories)
    print("Done inserting...")

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

### -------------- MySQL Client example Python --------------