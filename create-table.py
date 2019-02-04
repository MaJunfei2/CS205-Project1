import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "/Users/junfeima/Desktop/CS205-project1/car.db"
 
    sql_create_CarMake_table = """ CREATE TABLE IF NOT EXISTS CarMake (
                                        Make text PRIMARY KEY,
                                        CEO text NOT NULL,
                                        Country text NOT NULL
                                    ); """
 
    sql_create_Model_table = """CREATE TABLE IF NOT EXISTS Model (
                                    id integer PRIMARY KEY,
                                    Make text NOT NULL,
                                    Model text NOT NULL,
                                    Year integer NOT NULL,
                                    Engine_HP integer NOT NULL,
                                    Engine_Cylinders integer NOT NULL,
                                    Highway_MPG integer NOT NULL,
                                    City_MPG integer NOT NULL,
                                    FOREIGN KEY (Make) REFERENCES CarMake (Make)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_CarMake_table)
        # create tasks table
        create_table(conn, sql_create_Model_table)
        
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
    
