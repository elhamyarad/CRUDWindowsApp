import pyodbc
from Model.SaleModel import SaleModelClass


class Sales_DAL:

    def getStorsList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetStorList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def getTitlesList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetTitleList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def registerSale(self, SaleObject: SaleModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[RegisterSale] ?,?,?,?,?,?"
        params = (SaleObject._stor_id, SaleObject._ord_num, SaleObject._ord_date, SaleObject._qty,
                  SaleObject._payterms, SaleObject._title_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getSaleList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[GetSaleList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

    def deleteSale(self, stor_id:str, ord_num:str, title_id:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeleteSale] ?,?,?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (stor_id, ord_num, title_id,))
        connection.commit()

    def updateSale(self, SaleObject:SaleModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[UpdateSale] ?,?,?,?,?,?"
        params = (SaleObject._stor_id, SaleObject._ord_num, SaleObject._ord_date, SaleObject._qty,
                  SaleObject._payterms, SaleObject._title_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()
