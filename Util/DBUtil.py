import pyodbc

from .PropertyUtil import PropertyUtil

class DBUtil:

    conn = None

    @staticmethod
    def getDBConn():
        if DBUtil.conn is None:
            connectionString = PropertyUtil.getPropertyString()
            try:
                DBUtil.conn = pyodbc.connect(connectionString)
            except ConnectionError as err:
                print(f"Failed to establish connection: {err}")
        else:
            print("Connection already established")
        return DBUtil.conn
    
    @staticmethod
    def closeConnection():
        if DBUtil.conn is not None:
            DBUtil.conn.close()
            DBUtil.conn = None
        else:
            print("No such connection exists")
        return DBUtil.conn
    
    