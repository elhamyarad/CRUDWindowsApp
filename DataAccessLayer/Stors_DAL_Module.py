import pyodbc
from Model.StorModel import StorModelClass


class Stors_DAL:

    def registerStor(self, storObject: StorModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[RegisterStor] ?,?,?,?,?,?"
        params = (storObject._storId, storObject._storName, storObject._storeAddress, storObject._city,
                  storObject._state, storObject._zip)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getStorList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[GetStorList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

    def deleteStor(self, stor_id:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeleteStor] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (stor_id,))
        connection.commit()

    def updateStor(self, storObject:StorModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[UpdateStor] ?,?,?,?,?,?"
        params = (storObject._storId, storObject._storName, storObject._storeAddress, storObject._city,
                  storObject._state, storObject._zip)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()
