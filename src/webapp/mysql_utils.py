import mysql.connector
from mysql.connector import errorcode, Error

'''
self.conn = mysql.connector.connect(
        host="localhost",
        user="turtle",
        database="non_verbal_reasoning",
        passwd="turtle"
)
'''
class MySQL:
    def __init__(self):
        '''self.conn = mysql.connector.connect(
                host="nvrquiz-db-instance.chb3ppjrdtjp.ap-south-1.rds.amazonaws.com",
                port=3306,
                database="non_verbal_reasoning",
                user="turtle",
                password="NVRqu!z123"
        )'''
        self.conn = mysql.connector.connect(
                host="localhost",
                user="turtle",
                database="non_verbal_reasoning",
                passwd="turtle"
        )

        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def create_connection(self):
        '''self.conn = mysql.connector.connect(
                host="nvrquiz-db-instance.chb3ppjrdtjp.ap-south-1.rds.amazonaws.com",
                port=3306,
                database="non_verbal_reasoning",
                user="turtle",
                password="NVRqu!z123"
        )'''

        self.conn = mysql.connector.connect(
                host="localhost",
                user="turtle",
                database="non_verbal_reasoning",
                passwd="turtle"
        )

    def close_connection(self):
        self.conn.close()
    
    def create_cursor(self):
        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def close_cursor(self):
        self.curr.close()