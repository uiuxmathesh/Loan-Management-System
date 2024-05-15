

class PropertyUtil:

    @staticmethod
    def getPropertyString():
        SERVER_NAME = "Mathesh-PC"
        DATABASE_NAME = "LoanManager"
        TRUSTED_CONNECTION = "Yes"
        CONNECTION_STRING = f"Driver={{SQL Server}}; Server={SERVER_NAME}; Database={DATABASE_NAME}; Trusted_Connection={TRUSTED_CONNECTION}"
        return CONNECTION_STRING