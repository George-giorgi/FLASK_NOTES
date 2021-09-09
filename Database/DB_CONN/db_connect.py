import mysql.connector as myDbconneCt

def db_conneCt():
    credentials = {
            "host": "localhost",
            "user": "root",
            "database": "REACT_REDUX_FLASK_NOTES",
            "password": "Wagvl1chorchana123"
        }
    try:

        conn = myDbconneCt.connect(**credentials)
        cursor = conn.cursor()
        obj_dbConnect ={
            "connect": conn,
            "cursor": cursor
        }

        return obj_dbConnect
    except:

        return "problem from db server"


