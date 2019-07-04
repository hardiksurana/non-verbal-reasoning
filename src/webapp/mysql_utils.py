import mysql.connector
from mysql.connector import errorcode, Error

class MySQL:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host="localhost",
                user="turtle",
                database="non_verbal_reasoning",
                passwd="turtle"
        )

        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def __del__(self):
        self.curr.close()
        self.conn.close()
    
    