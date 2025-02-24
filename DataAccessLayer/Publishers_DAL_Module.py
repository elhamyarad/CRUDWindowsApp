import pyodbc
from Model.PublisherModel import PublisherModelClass


class Publishers_DAL:

    def registerPublisher(self, publisherObject: PublisherModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[RegisterPublisher] ?,?,?,?,?"
        params = (publisherObject._pubId, publisherObject._pubName, publisherObject._city, publisherObject._state,
                  publisherObject._country)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getPublisherList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[GetPublisherList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

    def deletePublisher(self, pub_id:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeletePublisher] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (pub_id,))
        connection.commit()

    def updatePublisher(self, publisherObject:PublisherModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[UpdatePublisher] ?,?,?,?,?"
        params = (publisherObject._pubId, publisherObject._pubName, publisherObject._city, publisherObject._state,
                  publisherObject._country)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()
