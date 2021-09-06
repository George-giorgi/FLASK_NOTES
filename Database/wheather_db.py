from logging import error
import mysql.connector as mydb
from wheather.amindi import req_api
from pprint import pp, pprint
import time

credentials = {
    "host": "localhost",
    "user": "root",
    "database": "REACT_REDUX_FLASK_NOTES",
    "password": "Wagvl1chorchana123"
}
g= 0
def update_wheather_db():
    data = req_api()
    conn = mydb.connect(**credentials)
    cursor = conn.cursor()

    _SQL = ("""UPDATE wheather SET
                CITY = %s,TEMP = %s, TM = %s, SKY = %s ,id = %s
                WHERE
                CITY = %s and id = %s""")
    for item in data:
        
        values = (item[1], item[2], item[3], item[4],item[0],item[1],item[0])
        cursor.execute(_SQL,values ) 
    pprint(data) 
    conn.commit()
    conn.close()
    
    
   
while True:
    try:
        g+=1
        update_wheather_db()
        print(g)
        
        time.sleep(60)
    except error:
        print(error)
        break