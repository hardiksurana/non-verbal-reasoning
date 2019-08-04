import mysql.connector
from mysql.connector import errorcode, Error

class MySQL:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host="<HOST_NAME>",
                port="<PORT_NUMBER>",
                database="<DB_NAME>",
                user="<USER_NAME>",
                password="<PASSWORD>"
        )

        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
                host="<HOST_NAME>",
                port="<PORT_NUMBER>",
                database="<DB_NAME>",
                user="<USER_NAME>",
                password="<PASSWORD>"
        )

    def close_connection(self):
        self.conn.close()
    
    def create_cursor(self):
        self.curr = self.conn.cursor(buffered=True, dictionary=True)
    
    def close_cursor(self):
        self.curr.close()