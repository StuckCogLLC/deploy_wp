###########
# mariadb database creation
###########

import sys
import getpass
import mariadb

#create and grant user
def create_grant(cur,dbuser,dbpass,dbname):
    try:
        print("Granting permissions to database")
        cur.execute(f"grant all privileges on {dbname}.* to {dbuser}@localhost identified by '{dbpass}';")
    except mariadb.Error as e:
        print(f"Error granting dbname: {dbname} to dbuser: {dbuser}")

#create database (wp core install expects this)
def create_database(cur,dbname):
    try:
        print("creating wp database")
        cur.execute(f"create database {dbname}")
    except mariadb.Error as e:
        print(f"Error creating: {dbname}")

def create_wpdbuser(dbuser,dbpass,dbname,ldbpass):
    try: 
        print("Connecting to Database")
        conn = mariadb.connect(
            host="localhost",
            port=3306,
            user="root",
            password=ldbpass)
        cur = conn.cursor()
        create_grant(cur,dbuser,dbpass,dbname)
        create_database(cur,dbname)
    except mariadb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

    conn.close()
