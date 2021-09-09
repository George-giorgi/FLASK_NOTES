import mysql.connector as myconnect
from .DB_CONN.db_connect import db_conneCt

class Person:
    
    def __init__(self, name=None, email=None, password=None):

        self.name = name
        self.email = email
        self.password = password
        
    def register(self):
        try:
            conn = db_conneCt()
            if conn != "problem from db server":
                
                cursor = conn["cursor"]
                cursor.execute("""INSERT INTO register(name, email, password) 
                                VALUES
                                (%s, %s, %s)""",(self.name, self.email, self.password))
                conn["connect"].commit()
                conn["connect"].close()
                return "Successful registration"
            else:
                return conn
        except:

            return "Email has already been used"

        
class Database:
    def __init__(self, email, password):

        self.email = email
        self.password = password

    def loggin(self):
        conn = db_conneCt()
        cursor = conn["cursor"]
        cursor.execute("""SELECT name, email, password FROM register
                        WHERE email = %s """,(self.email,))
        data = cursor.fetchone()
        
        conn["connect"].commit()
        conn["connect"].close()

        return data
    

class Note_Db:
    def __init__(self, email = None, note= None, time= None, important= None):
        self.email = email
        self.note = note
        self.time = time
        self.important = important 
        
    def add_note(self):
        conn = db_conneCt()
        cursor = conn["cursor"]
        
        _SQL = ("""INSERT INTO notes(user_email, note, insert_time, important) 
                                        VALUES (%s, %s, %s, %s)
                                        """)
        values = (self.email, self.note, self.time, self.important)
        cursor.execute(_SQL, values)
                
        conn["connect"].commit()
        conn["connect"].close()
    
    def del_note(self):
        conn = db_conneCt()
        cursor = conn["cursor"]
        _SQL = ("""DELETE FROM notes
                WHERE user_email = %s and insert_time = %s""")
                                                     
        values = (self.email, self.time)
        cursor.execute(_SQL, values)
        
        conn["connect"].commit()
        conn["connect"].close()

    def update_inp_cont(self, time, email, condition):
        conn = db_conneCt()
        cursor = conn["cursor"]
        if condition == "changeImportant":
            _SQL = ("""UPDATE notes SET insert_time = %s, important = %s
                        WHERE insert_time = %s and user_email = %s and note = %s """)
            values = (self.time, self.important, time, email, self.note )
            cursor.execute(_SQL, values)
        elif condition == "changeContent":
            
            _SQL =("""UPDATE notes SET insert_time = %s, note = %s
                    WHERE insert_time = %s and user_email = %s""")
            values = (self.time, self.note, time, email, )
            cursor.execute(_SQL, values)
            
        conn["connect"].commit()
        conn["connect"].close()
            
    def get_all(self):
        conn = db_conneCt()
        cursor = conn["cursor"]
        cursor.execute("""SELECT * from notes 
                        WHERE user_email = %s""",(self.email,))
        data = cursor.fetchall()

        return data



        
        

        


        
        