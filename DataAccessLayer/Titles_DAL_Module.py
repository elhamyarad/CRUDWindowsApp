import pyodbc
from Model.TitlesModel import TitlesModelClass


class Titles_DAL:

    def getTypesList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetTypesList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def getAuthorList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetAuthorList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def getPublishersList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetPublisherList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def registerTitle(self, TitleObject: TitlesModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[RegisterTitle] ?,?,?,?,?,?,?,?,?,?"
        params = (TitleObject._title_Id, TitleObject._title, TitleObject._type, TitleObject._pubid,
                  TitleObject._price, TitleObject._advance, TitleObject._royalty, TitleObject._ytdsales, TitleObject._notes,
                  TitleObject._pubdate)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getTitleList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[GetTitleList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

    def deleteTitle(self, title_Id:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeleteTitles] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (title_Id,))
        connection.commit()

    def deleteTitleAuthor(self, title_Id:str, au_Id:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeleteTitleAuthor] ?,?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (title_Id, au_Id,))
        connection.commit()

    def addTitleAuthor(self, au_Id:str, title_Id:str, au_ord:int, royaltyper:int):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[AddTitleAuthor] ?,?,?,?"
        params = (au_Id, title_Id, au_ord, royaltyper)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def updateTitle(self, TitleObject:TitlesModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[UpdateTitle] ?,?,?,?,?,?,?,?,?,?"
        params = (TitleObject._title_Id, TitleObject._title, TitleObject._type,TitleObject._pubid,
                  TitleObject._price, TitleObject._advance, TitleObject._royalty, TitleObject._ytdsales, TitleObject._notes,
                  TitleObject._pubdate)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getTitleAuthor(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetTitleAuthor"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows
