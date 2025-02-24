import pyodbc
from Model.EmployeeModel import EmployeeModelClass


class Employees_DAL:

    def getJobList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetJobList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows

    def getPublisherList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "execute GetPublisherList"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()
        return rows


    def registerEmployee(self, EmployeeObject: EmployeeModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[RegisterEmployee] ?,?,?,?,?,?,?,?"
        params = (EmployeeObject._emp_Id, EmployeeObject._empFirstName, EmployeeObject._empminit, EmployeeObject._empLastName,
                  EmployeeObject._empjobId, EmployeeObject._empjobLevel, EmployeeObject._emppubId, EmployeeObject._empHireDate)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getEmployeeList(self):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[GetEmployeeList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

    def deleteEmployee(self, emp_Id:str):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC	[dbo].[DeleteEmployee] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, (emp_Id,))
        connection.commit()

    def updateEmployee(self, EmployeeObject:EmployeeModelClass):
        connectionString = "Driver={SQL Server};Server=LENOVO;DataBase=pubs;Trusted_Connection=yes"
        commandText = "EXEC [dbo].[UpdateEmployee] ?,?,?,?,?,?,?,?"
        params = (EmployeeObject._emp_Id, EmployeeObject._empFirstName, EmployeeObject._empminit, EmployeeObject._empLastName,
                  EmployeeObject._empjobId, EmployeeObject._empjobLevel, EmployeeObject._emppubId, EmployeeObject._empHireDate)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()
