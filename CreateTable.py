import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    
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
    database = "car.db"
 
    sql_create_CarMake_table = """ CREATE TABLE IF NOT EXISTS tblCarMake(
                                        pmkMake text PRIMARY KEY,
                                        fldCEO text NOT NULL,
                                        fldCountry text NOT NULL
                                     ); """
 
    sql_create_Model_table = """CREATE TABLE IF NOT EXISTS tblModel (
                                    PMKid integer PRIMARY KEY,
                                    fnkMake text NOT NULL,
                                    fldModel text NOT NULL,
                                    fldYear integer NOT NULL,
                                    fldEngine_HP integer NOT NULL,
                                    fldEngine_Cylinders integer NOT NULL,
                                    fldHighWay_MPG integer NOT NULL,
                                    fldCity_MPG integer NOT NULL,
                                    FOREIGN KEY (fnkMake) REFERENCES CarMake (pmkMake)
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
