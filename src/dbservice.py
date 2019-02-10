import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_person(conn, person):
    #Create new entry into Person table
    sql = ''' INSERT INTO Person(name, age, creationEpochTime)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, person)
    return cur.lastrowid

def count_person(conn):
    #Create new entry into Person table
    sql = ''' SELECT count(*) FROM PERSON '''
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()
    
    return result[0]