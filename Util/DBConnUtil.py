import pyodbc

from .PropertyUtil import PropertyUtil

class DBConnUtil:
    conn = None

    def __init__(self):
        self.connection = self.getConnection()
        self.cursor = self.connection.cursor()

    def close(self):
        self.closeConnection()
    
    def getConnection(self):
        if self.conn is None:
            connectionString = PropertyUtil.getPropertyString()
            try:
                self.conn = pyodbc.connect(connectionString)
            except ConnectionError as err:
                print(f"Failed to establish connection: {err}")
        else:
            print("Connection already established")
        return self.conn


    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        
        else:
            print("No such connection exists")
        return self.conn