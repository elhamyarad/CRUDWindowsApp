import pyodbc
from Model.AuthorModel import AuthorModelClass


class Authors_DAL:
    # def getCityList(self):
    #     connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
    #     commandText = "execute GetCityList"
    #     connection = pyodbc.connect(connectionString)
    #     cursor = connection.cursor()
    #     cursor.execute(commandText)
    #     rows = cursor.fetchall()
    #     return rows
    #
    # def getStateList(self):
    #     connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
    #     commandText = "execute GetStateList"
    #     connection = pyodbc.connect(connectionString)
    #     cursor = connection.cursor()
    #     cursor.execute(commandText)
    #     rows = cursor.fetchall()
    #     return rows

    def registerAuthor(self, authorObject: AuthorModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[RegisterAuthor] ?,?,?,?,?,?,?,?,?"
        params = (authorObject._auId, authorObject._auLastName, authorObject._auFirstName, authorObject._auPhone,
                  authorObject._auAddress, authorObject._auCity, authorObject._auState, authorObject._auZip,
                  authorObject._auContract)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getAuthorList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetAuthorList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def deleteAuthor(self, auId:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeleteAuthor] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (auId,))
        connection.commit()

    def updateAuthor(self, authorObject:AuthorModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[UpdateAuthor] ?,?,?,?,?,?,?,?,?"
        params = (authorObject._auId, authorObject._auLastName, authorObject._auFirstName, authorObject._auPhone,
                  authorObject._auAddress, authorObject._auCity, authorObject._auState, authorObject._auZip,
                  authorObject._auContract)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()
