import mysql.connector
from mysql.connector import errorcode, Error

class MySQL:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host="nvrquiz-db-instance.chb3ppjrdtjp.ap-south-1.rds.amazonaws.com",
                port=3306,
                database="non_verbal_reasoning",
                user="turtle",
                password="NVRqu!z123"
        )

        # self.conn = mysql.connector.connect(
        #         host="localhost",
        #         user="turtle",
        #         database="non_verbal_reasoning",
        #         passwd="turtle"
        # )

        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def __del__(self):
        self.curr.close()
        self.conn.close()
    
    